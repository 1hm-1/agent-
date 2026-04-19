import os, json
from typing import Sequence
from langchain_core.messages import message_to_dict, messages_from_dict
from langchain_core.chat_history import BaseChatMessageHistory, BaseMessage
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(storage_path, f"{session_id}.json")
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
            
    def add_messages(self, message: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(message)
        # 将消息转换为字典列表并保存到文件
        new_messages=[]
        for msg in all_messages:
            new_messages.append(message_to_dict(msg))
        # 将消息列表保存到文件中
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f, ensure_ascii=False, indent=4)
            
    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f: 
                messages_dict = json.load(f)
                return messages_from_dict(messages_dict)
        except FileNotFoundError:
            return []
        
    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
            
            

model = ChatTongyi(model="qwen3-max")
prompt =  PromptTemplate.from_template(
    "你需要根据对话历史回应用户问题。对话历史:{chat_history} 用户问题:{input},请给出回应"
)
base_chain = prompt | model |  StrOutputParser()

store = {}

def get_history(session_id):
    return FileChatMessageHistory(session_id, storage_path="./chat_history")
    
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
    # res1 = conversation_chain.invoke({"input": "左边有3棵树"}, session_config)
    # print("第一次执行:",res1)
    # res2 = conversation_chain.invoke({"input": "右边有65棵树"}, session_config)
    # print("第二次执行:",res2)
    res3 = conversation_chain.invoke({"input": "一共有多少棵树"}, session_config)
    print("第三次执行:",res3)