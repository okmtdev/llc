from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4o-mini")
messages = [
    SystemMessage(content="あなたは優秀なアシスタントです。"),
    HumanMessage(content="日本で最も高い山は何ですか？")
]
response = llm.invoke(messages)
print(response.content)
