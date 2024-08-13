
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

# The below dummy function is calling deployed model and generate an output joke 
# def dummy(country, keyword="dummy no keyword"):
# 	output = query({
# 	"inputs": "<s> [INST] You are a joke generator. I want a joke related to " + country + " with a quality of 5 out of 5 stars and not offensive. [/INST] ",
# 	"parameters": {}
# 	})
# 	print(output)
# 	return str(output)

def dummy(country, keyword="dummy no keyword"):
    # Simulated output from the query function
    output = [{'generated_text': '<s> [INST] You are a joke generator. I want a joke related to India with a quality of 5 out of 5 stars and not offensive. [/INST] Why did the Indian man go to the doctor? Because he was feeling a little bit "spicy"! </s>'}]
    # output = query({
	# "inputs": "<s> [INST] You are a joke generator. I want a joke related to " + country + " with a quality of 5 out of 5 stars and not offensive. [/INST] ",
	# "parameters": {}
	# })

    # Extract the generated text
    generated_text = output[0]['generated_text']
    
    # Find the start and end of the joke
    start = generated_text.find('[/INST] ') + len('[/INST] ')
    end = generated_text.find('</s>')
    
    # Extract the joke
    joke = generated_text[start:end].strip()
    
    print(joke+"hihi")
    return joke

# Test the function
# dummy("India")



