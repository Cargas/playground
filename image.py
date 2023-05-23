import config
import openai
import os
import sys
import urllib

from datetime import datetime

openai.api_key = config.api_key

if len(sys.argv) < 2:
    print("Error: No image prompt provided.")
    exit(2)

prompt = ""
for arg in sys.argv[1:]:
    prompt += arg + ' '

# Cut off the last space
prompt = prompt[:-1]

images_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "images")
if not os.path.exists(images_path):
    os.mkdir(images_path)

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

file_name_prompt = prompt
# Don't save prompt as image name if it is too long.
if 100 < len(prompt):
    file_name_prompt = prompt[:100].strip()
    
file_name_prompt += " "

# Assign int value to name, check if image with the same name already exists.
count = 1
file_name = file_name_prompt + str(count) + ".jpg"
while os.path.exists(os.path.join(images_path, file_name)):
    count += 1
    file_name = file_name_prompt + str(count) + ".jpg"

urllib.request.urlretrieve(image_url, os.path.join(images_path, file_name))

log_path = os.path.join(images_path, "log.txt")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_path, "a") as file:
    file.write(f"{timestamp}: {prompt}\n")

print("Image saved as " + file_name)