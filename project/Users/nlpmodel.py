
import requests

API_URL = "https://ci8b86d3ag2wz0in.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json" 
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# 	"parameters": {}
# })

def dummy(country, keyword="dummy no keyword"):
	output = query({
	"inputs": "<s> [INST] You are a joke generator. I want a joke related to " + country + " with a quality of 5 out of 5 stars and not offensive. [/INST] ",
	"parameters": {}
	})
	print(output)
	return str(output)


