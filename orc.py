from Image_to_Base64 import Img_to_Base64
from json_request import web_request
import json

import urllib
import urllib.request

client_id = 'qMNUvwPNLPZacuEsO4sWVaYe'
client_secret = 'XLB48cEg9gsTgSz3EHuFiixW5AT4h0bP'


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret + ''
print(host)
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
str_content = json.loads(content)
access_token = str_content["access_token"]
if (content):
    print(access_token)

img_address = input("请输入图片地址:")

img_base64 = Img_to_Base64(img_address)
str_img = img_base64.image_to_base64()

js_req = web_request(str_img, access_token)
json_req = js_req.json_request()

print(json_req)
print(json_req['words_result'])
for i in range(json_req['words_result_num']):
    print(json_req['words_result'][i]['words'])


# print(str_img)
