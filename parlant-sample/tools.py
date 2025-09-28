import os
from parlant import Parlant
from parlant.guidelines import Guidelines
from langchain_openai import ChatOpenAI
from langchain_community.llms.huggingface_text_gen import HuggingFaceTextGen # HuggingFaceの例

# (1) LLMのインスタンスを作成
# ChatOpenAIの例
# os.environ["OPENAI_API_KEY"] = "あなたのOpenAI APIキー"
llm = ChatOpenAI(model="gpt-4o-mini")

# HuggingFaceの例
# llm = HuggingFaceTextGen(model_id="google/flan-t5-large")

# (2) Parlantのガイドラインを定義
# ユーザー入力に対して、LangChainで定義したツールを呼び出すルール
guidelines = Guidelines.from_dict({
    "actions": {
        "on_user_input": [
            {"call_tool": {"name": "web_search_tool", "query": "{{ user_input }}"}}
        ]
    }
})

# (3) Parlantのインスタンスを作成
# ここでLLM、ツール、ガイドラインを組み合わせます
parlant = Parlant(llm=llm, guidelines=guidelines, tools=tools)

# (4) Parlantにユーザーの質問を処理させる
print("--- Parlant 実行開始 ---")
user_question = "大谷翔平の最新の活躍について教えて"
print(f"ユーザーの質問: {user_question}\n")

response = parlant.run(user_question)

print("\n--- Parlant 実行結果 ---")
print(response.output)