import os
import sys
from pydantic import BaseModel

sys.stderr.write(f"[DEBUG] sys.path = {sys.path}\n")
sys.stderr.write(f"[DEBUG] current dir = {os.getcwd()}\n")

# MCP Server Entery
from fastmcp import FastMCP

# Message definitions (imported from base.py)
from prompts.base import Message, UserMessage, AssistantMessage

# Create MCP instance
mcp = FastMCP("My App", dependencies=["pandas", "numpy"])

sys.stderr.write("[DEBUG] FastMCP instance created.\n")

# -------------------------------
# Pydantic model definitions
# -------------------------------
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
def debug_session_start(error_message: str) -> list[Message]:
    """Initiates a debugging help session."""
    return [
        UserMessage(f"I encountered an error:\n{error_message}"),
        AssistantMessage("Okay, I can help with that. Can you provide the full traceback and tell me what you were trying to do?")
    ]

mcp

sys.stderr.write("[DEBUG] mcp object is referenced and ready.\n")