import requests
import openai

API_URL = "https://a6g4w0nkhxi9aat9.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

#function 0 fake
def dummy(country):
    return country
#end of function 0

#function 1 llama
# def dummy(country, keyword="dummy no keyword"):
#     # Simulated output from  query function
#     output = query({
# 	"inputs": "<s> [INST] You are a joke generator. I want a joke related to " + country + " with a quality of 5 out of 5 stars and not offensive. [/INST] ",
# 	"parameters": {}
# 	})

#     # Extract the generated text
#     generated_text = output[0]['generated_text']

#     # Find the start and end of the joke
#     start = generated_text.find('[/INST] ') + len('[/INST] ')
#     end = generated_text.find('</s>')

#     # Extract the joke
#     joke = generated_text[start:end].strip()

#     print(joke+"hihi")
#     return joke
#end of function 1

#function 2 gpt
# def dummy(country):
#     response = openai.ChatCompletion.create(
#         model="ft:gpt-3.5-turbo-0125:personal:msia-jokes:A8AJXqTB",
#         messages=[
#             {"role": "system", "content": "You are a joke generator and make it related to the country mentioned."},  # Optionally customize this
#             {"role": "user", "content": f"Write a funny joke about {country}. It can relate in terms of landmark or food. Only one"}
#         ],
#         max_tokens=2048
#     )

# # Print the generated joke
#     return response['choices'][0]['message']['content'].strip()
# end of function 2     



