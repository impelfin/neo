import os
import sys
from PIL import Image as PILImage
from urllib.parse import urlparse, unquote
from openai import AsyncOpenAI
import httpx
from pydantic import BaseModel
import io
import json
    
sys.stderr.write(f"[DEBUG] sys.path = {sys.path}\n")
sys.stderr.write(f"[DEBUG] current dir = {os.getcwd()}\n")

from fastmcp import FastMCP, Context

from prompts.base import Message, UserMessage, AssistantMessage

SECRET_PATH = os.path.join(os.path.dirname(__file__), 'secret.json')
try:
    with open(SECRET_PATH, 'r') as f:
        secret = json.load(f)
    OPENAI_API_KEY = secret.get('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is missing in secret.json.')
except FileNotFoundError:
    raise RuntimeError('secret.json file not found.')
except json.JSONDecodeError:
    raise RuntimeError('secret.json file is malformed.')

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

mcp = FastMCP("FastMCP Example", dependencies=["pandas", "numpy"])

sys.stderr.write("[DEBUG] FastMCP instance created.\n")


# -------------------------------
# Pydantic model definitions
# -------------------------------

class ImageData(BaseModel):
    data: bytes
    format: str = 'png'

class UserInfo(BaseModel):
    user_id: int
    notify: bool = False


# -------------------------------
# Tools
# -------------------------------

@mcp.tool()
async def send_notification(user: UserInfo, message: str) -> dict:
    """Sends a notification to a user if requested."""

    if user.notify:
        sys.stderr.write(f"Notifying user {user.user_id}: {message}\n")
        return {"status": "sent", "user_id": user.user_id}
    return {"status": "skipped", "user_id": user.user_id}

@mcp.tool()
def get_stock_price(ticker: str) -> float:
    """Gets the current price for a stock ticker."""
    
    prices = {"AAPL": 180.50, "GOOG": 140.20}
    return prices.get(ticker.upper(), 0.0)


# -------------------------------
# Resources
# -------------------------------

@mcp.resource("config://app-version")
def get_app_version() -> str:
    return "v2.1.0"

@mcp.resource("db://users/{user_id}/email")
async def get_user_email(user_id: str) -> str:
    emails = {"123": "alice@example.com", "456": "bob@example.com"}
    return emails.get(user_id, "not_found@example.com")

@mcp.resource("data://product-categories")
def get_categories() -> list[str]:
    return ["Electronics", "Books", "Home Goods"]


# -------------------------------
# Prompts
# -------------------------------

@mcp.prompt()
def ask_review(code_snippet: str) -> str:
    """Generates a standard code review request."""
    return f"Please review the following code snippet for potential bugs and style issues:\n```python\n{code_snippet}\n```"

@mcp.prompt()
def debug_session_start(error_message: str) -> list[dict]:
    """Initiates a debugging help session."""
    return [
        {
            "role": "user",
            "content": f"I encountered an error:\n{error_message}"
        },
        {
            "role": "assistant",
            "content": "Okay, I can help with that. Can you provide the full traceback and tell me what you were trying to do?"
        }
    ]


# -------------------------------
# Context Resources & Tools
# -------------------------------

@mcp.resource("system://status/{system_id}")
async def get_system_status(system_id: str) -> dict:
    """Checks system status and logs information."""
    return {"status": "OK", "load": 0.5, "system": system_id}

@mcp.tool()
async def process_large_file(file_uri: str, ctx: Context) -> str:
    """Processes a large file, reporting progress and reading resources. Supports both MCP resource URIs and file:/// URIs."""
    await ctx.info(f"Starting processing for {file_uri}")
    file_content = None

    if file_uri.startswith("file://"):
        import os
        from urllib.parse import urlparse, unquote
        parsed = urlparse(file_uri)
        path = unquote(parsed.path)
        if not os.path.exists(path):
            await ctx.error(f"File not found: {path}")
            return f"File not found: {path}"
        with open(path, "r", encoding="utf-8") as f:
            file_content = f.read()
    else:
        file_content_resource = await ctx.read_resource(file_uri)
        file_content = file_content_resource[0].content  

    lines = file_content.splitlines()
    total_lines = len(lines)

    for i, line in enumerate(lines):
        if (i + 1) % 100 == 0:  
            await ctx.report_progress(i + 1, total_lines)

    await ctx.info(f"Finished processing {file_uri}")
    return f"Processed {total_lines} lines."


# -------------------------------
# Image Tools
# -------------------------------

@mcp.tool()
def create_thumbnail(image_data) -> str:
    """
    Creates a 100x100 thumbnail from the provided image.
    Saves it as '<original_filename>_thumbnail.<extension>' and returns the file path.
    Supports both file:/// and plain local file paths as input.
    """

    if isinstance(image_data, str):
        if image_data.startswith("file://"):
            parsed = urlparse(image_data)
            path = unquote(parsed.path)
        else:
            path = image_data
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {path}")
        with open(path, "rb") as f:
            img_bytes = f.read()
        img = PILImage.open(io.BytesIO(img_bytes))
        base, ext = os.path.splitext(os.path.basename(path))
        output_path = os.path.join(os.path.dirname(path), f"{base}_thumbnail{ext}")
    elif isinstance(image_data, ImageData):
        img = PILImage.open(io.BytesIO(image_data.data))
        output_path = "thumbnail.png"
    else:
        raise ValueError("image_data must be an ImageData object or a file path string")
    img.thumbnail((100, 100))
    img.save(output_path, format="PNG")
    img.show()
    return output_path

@mcp.tool()
def load_image_from_disk(path: str) -> str:
    """
    Loads an image from the specified path (supports file:///), 
    saves it as '<original_filename>_loaded.<extension>', 
    shows the image, and returns the file path.
    """
    
    if isinstance(path, str) and path.startswith("file://"):
        parsed = urlparse(path)
        real_path = unquote(parsed.path)
    else:
        real_path = path
    if not os.path.exists(real_path):
        raise FileNotFoundError(f"Image file not found: {real_path}")
    with open(real_path, 'rb') as f:
        data = f.read()
    base, ext = os.path.splitext(os.path.basename(real_path))
    output_path = os.path.join(os.path.dirname(real_path), f"{base}_loaded{ext}")
    with open(output_path, 'wb') as f:
        f.write(data)
    img = PILImage.open(io.BytesIO(data))
    img.show()
    return output_path


# -------------------------------
# LLM Sampling
# -------------------------------

@mcp.tool()
async def generate_poem(topic: str, context: Context) -> str:
    """Generate a short poem about the given topic."""

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a talented poet who writes concise, evocative verses."},
            {"role": "user", "content": f"Write a short poem about {topic}"}
        ]
    )
    return response.choices[0].message.content

@mcp.tool()
async def summarize_document(document: str, context: Context) -> str:
    """Summarize a document using server-side LLM capabilities.
    
    Args:
        document: Either a resource URI (e.g., 'system://docs/example.txt') or the actual document content
        context: The MCP context
    
    Returns:
        A concise summary of the document
    """

    if document.startswith(('system://', 'config://', 'db://', 'data://')):        
        try:
            doc_resource = await context.read_resource(document)
            content = doc_resource[0].content  
        except Exception as e:
            return f"Error reading resource: {str(e)}"
    else:
        content = document
    
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert summarizer. Create a concise summary."},
            {"role": "user", "content": f"Summarize the following document:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content


mcp

sys.stderr.write("[DEBUG] mcp object is referenced and ready.\n")
