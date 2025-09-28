from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
import os

# メモリを初期化
# 過去の会話をすべて記憶します
memory = ConversationBufferMemory(return_messages=True)

# LLMを初期化
llm = ChatOpenAI(model="gpt-4o-mini")

# 会話チェーンを初期化
# LLMとメモリを組み合わせます
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# 最初の質問
print("AI: こんにちは！何かお手伝いできることはありますか？")
user_input1 = "日本の首都はどこですか？"
print(f"あなた: {user_input1}")
ai_response1 = conversation.invoke(user_input1)
print(f"AI: {ai_response1['response']}")

# 次の質問（前の会話の文脈に依存）
user_input2 = "そこに住んでいる人の数は？" # 「そこ」は「日本の首都」を指す
print(f"あなた: {user_input2}")
ai_response2 = conversation.invoke(user_input2)
print(f"AI: {ai_response2['response']}")

# メモリに保存された会話履歴を出力
print("\n--- メモリに保存された会話履歴 ---")
print(memory.load_memory_variables({}))