import openai
import base64
from IPython.display import Image, display
from pathlib import Path

org_img_file = './data/org_image_for_edit.png'
mask_img_file = './data/mask_image_for_edit.png' 

with open(org_img_file, 'rb') as image_file, open(mask_img_file, 'rb') as mask_file:
    response = openai.images.edit(
        model="dall-e-2", 
        image=image_file,
        mask=mask_file,
        prompt="Happy robots swimming in the water",
        n=1,
        size="512x512",
        response_format="b64_json"
    )

b64_image = response.data[0].b64_json

display(Image(data=base64.b64decode(b64_image)))

with open('./data/edited_image.png', 'wb') as f:
    f.write(base64.b64decode(b64_image))

print("이미지가 'edited_image.png'로 저장되었습니다.")