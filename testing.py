# import requests

# API_URL = "https://ci8b86d3ag2wz0in.us-east-1.aws.endpoints.huggingface.cloud"
# headers = {
# 	"Accept" : "application/json",
# 	"Content-Type": "application/json" 
# }

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# output = query({
# 	"inputs": "<s>[INST] You are a joke generator. I want a joke related to China with a quality of 5 out of 5 stars and not offensive. [/INST]",
# 	"parameters": {}
# })
output = [{'generated_text': '<s>[INST] You are a joke generator. I want a joke related to China with a quality of 5 out of 5 stars and not offensive. [/INST] Why did the Chinese man go to the doctor? Because he was feeling a little "sick" of the food in China!</s>'}]

generated_text = output[0]['generated_text']

# Remove the beginning and ending markers and the instruction part
start_idx = generated_text.find("[/INST]") + len("[/INST] ")
end_idx = generated_text.find("</s>")
print(start_idx)
print(end_idx)
joke = generated_text[start_idx:end_idx].strip()
print(joke)
#print(output)