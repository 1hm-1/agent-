from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen3-max")
prompt =  PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender},帮我起个名字，简单回答"
)

chain = prompt | model | StrOutputParser() | model | StrOutputParser()

res = chain.invoke({"lastname": "张", "gender": "儿子"})

# model输出的类型为AIMessage，StrOutputParser将其转换为字符串，再输入到model中，最后输出字符串结果

print(type(res), res)