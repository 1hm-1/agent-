from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender},帮我起个名字，简单回答"
)

model = Tongyi(model="qwen-max")

chain = prompt_template | model

res = chain.invoke({"lastname": "张",  "gender": "儿子"})
print(res) 

