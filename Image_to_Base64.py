import base64
from io import BytesIO

# pip3 install pillow
from PIL import Image


class Img_to_Base64:

    def __init__(self, image_path):
        self.image_path = image_path

    # 若img.save()报错 cannot write mode RGBA as JPEG
    # 则img = Image.open(image_path).convert('RGB')
    def image_to_base64(self):
        img = Image.open(self.image_path).convert('RGB')
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data)
        print(base64_str)
        return base64_str
