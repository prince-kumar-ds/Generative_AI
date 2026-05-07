from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatAnthropic(model='gpt-4')

result = model.invoke('What is Self- Attention in Trasformers')

print(result.content)

