import openai

image = open("image.png", "rb")
mask = open("mask.png", "rb")

response = openai.Image.create_edit(
    image=image,
    mask=mask,
    prompt="many apples in cardboard box",
    n=1,
    size="512x512"
)
image_url = response["data"][0]["url"]
print(image_url)
