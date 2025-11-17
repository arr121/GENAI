import os
import openai
from dotenv import load_dotenv
from openai import OpenAI
import re
load_dotenv()

openai.api_key= os.getenv("OPENAI_API_KEY")
client = OpenAI()
def create_shopping_list(receipe):
    prompt= f"List out the shopping items required as part of receipe and instruct me the cooking process for the : {receipe} "
    return prompt

receipe = create_shopping_list("Hyderabadi Dum Biriyani")

print(receipe)

# Receaching out to OpenAI for the answer
respone = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", 
            "content": receipe
         }
    ],
    temperature=0.7,
    top_p=1,
    n=1,
)
print(respone.choices[0].message.content)

# Putting the ingredients into a shopping list
shopping_list= []
text= respone.choices[0].message.content
if text is None:
    text = ""
pattern= re.compile(r'-(.*)')
matches = pattern.findall(text)
print("Shopping List:",matches)
for match in matches:
    print(match.strip())
    shopping_list.append(match.strip())

print("Final Shopping List:",shopping_list)


# Sending the item to DALLE to create images for each item
if shopping_list:
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=shopping_list[0],
        size="1024x1024",
        quality="standard",
        n=1,
    )
    if image_response and image_response.data:
        image_url = image_response.data[0].url
        print("Image URL for", shopping_list[0], ":", image_url)
    else:
        print("Failed to generate image")
else:
    print("No shopping list items found")
