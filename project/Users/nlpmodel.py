# from huggingface_hub import hf_hub_download
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain
# import os

# HUGGINGFACEHUB_API_TOKEN = "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"

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN 

# template = '''generate me a joke: {chat}

# '''

# prompt = PromptTemplate(
#     input_variables=["chat"],
#     template=template
# )

# llm = HuggingFaceHub(repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
#     model_kwargs= {'temperature': 0.2, 'max_length': 50})

# chain = LLMChain(llm=llm, prompt=prompt)
# result = chain.run(chat="indian")
# print(result)



def dummy(country, keyword="dummy no keyword"):
    #change country short form to full 
    return keyword + " jokes generated for country " + country

