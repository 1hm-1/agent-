from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatTongyi(model="qwen3-max")

messages = [
    SystemMessage("你是一个边塞诗人"),
    HumanMessage("写一首唐诗"),
    AIMessage("锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage("按照上一句回复的格式再写一首唐诗")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end="")