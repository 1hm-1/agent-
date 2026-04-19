from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")
res = model.invoke("请介绍一下自己")
print(res)