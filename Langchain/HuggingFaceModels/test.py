from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
    task="text-generation",
    pipeline_kwargs= dict(temperature=0.5,
    max_new_token=100
)

model = ChatHuggingFace(llm=llm)


result = model.invoke("What is Postional Encoding in Transformers")

print(result.content)