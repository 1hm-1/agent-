from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi


def print_prompt(full_prompt):
    print("="*20, full_prompt.to_string(), "="*20)
    return full_prompt

model = ChatTongyi(model="qwen3-max")
prompt =  PromptTemplate.from_template(
    "你需要根据对话历史回应用户问题。对话历史:{chat_history} 用户问题:{input},请给出回应"
)
base_chain = prompt | print_prompt | model |  StrOutputParser()

store = {}

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
    
#创建一个新的链，对原有链增强功能：自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,  #通过会话id获取InMemoryChatMessageHistory对象
    input_message_key="input",
    history_messages_key="chat_history",
)

if __name__ == "__main__":
    session_config={
        "configurable": {
            "session_id": "user01"
        }
    }
    res1 = conversation_chain.invoke({"input": "左边有3棵树"}, session_config)
    print("第一次执行:",res1)
    res2 = conversation_chain.invoke({"input": "右边有65棵树"}, session_config)
    print("第二次执行:",res2)
    res3 = conversation_chain.invoke({"input": "一共有多少棵树"}, session_config)
    print("第三次执行:",res3)