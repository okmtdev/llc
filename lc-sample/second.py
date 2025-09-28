from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
# プロンプトテンプレートを定義
# このテンプレートが、LLMに与える指示とユーザーの入力を組み合わせる役割を担います
joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたはプロのコメディアンです。指定されたテーマで面白いジョークを作成してください。"),
    ("human", "テーマ：{topic}")
])

# LLMとプロンプトを組み合わせたチェーンを作成
# これが「ユーザー入力 -> プロンプト -> LLM -> 出力」という一連の流れを定義します
joke_chain = LLMChain(
    llm=llm,
    prompt=joke_prompt,
    verbose=True  # 実行プロセスを表示
)

# チェーンを実行
# "topic"というキーにテーマを渡します
response = joke_chain.invoke({"topic": "猫"})

print("\n--- 生成されたジョーク ---")
print(response['text'])