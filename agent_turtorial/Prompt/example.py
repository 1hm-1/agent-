from openai import OpenAI
client = OpenAI(
    base_url = "https://api.deepseek.com"
)

example_data = {
    "是": [
        ("公司ABC发布季度财报，显示收入增长了20%。", "公司ABC发布季度财报，显示利润上升"),
        ("公司XYZ宣布裁员计划，预计将裁员500人。", "公司XYZ招聘需求萎缩。")
    ],
    "否": [
        ("黄金价格下跌，投资者抛售", "外汇市场交易额创下新高"),
        ("央行降息，刺激经济增长", "新能源技术的创新")
    ]
}

questions = [
    ("利率上升，影响房地产市场。", "利率上升会导致房地产市场需求下降。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势更加明显"),
    ("股票市场今日大涨，投资者乐观情绪高涨。", "持续上涨的市场让投资者信心增强。")
]

messages = [
    {"role": "system", "content": f"你帮我完成文本匹配，给你两个句子，被[]包围，你判断他们是否匹配，回答是或不是，请参考如下示例："}
]

for key, value in example_data.items():
    for pair in value:
        messages.append({"role": "user", "content": f"句子1：[{pair[0]}]，句子2：[{pair[1]}]"})
        messages.append({"role": "assistant", "content": key})
        

for q in questions:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages+[
            {"role": "user", "content": f"句子1: [{q[0]}]，句子2: [{q[1]}]"}
        ]
    )

    print(response.choices[0].message.content)  