import openai 
from IPython.display import Image, display

org_img_file = './data/org_image_for_variation.png'

response = openai.Image.create_variation(
    image = open(org_img_file, 'rb'),
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']
print(image_url)
display(Image(url=image_url))
print('-' * 50)