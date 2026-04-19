from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

example_template = PromptTemplate.from_template("单词：{word}，反义词：{antonym}")

example_data = [
    {"word": "高兴", "antonym": "难过"},
    {"word": "大", "antonym": "小"},
    {"word": "快", "antonym": "慢"},
]
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="告知我单词的反义词，提供如下示例",
    suffix="基于前面的示例，{input_word}的反义词是什么？",
    input_variables=["input_word"]
)

prompt_text = few_shot_template.invoke({"input_word": "漂亮"}).to_string()
#print(prompt_text)

model = Tongyi(model="qwen-max")
res = model.stream(input=prompt_text)
for chunk in res:
    print(chunk, end="")