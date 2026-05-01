from llm import Myllm
from tools import calcultor
from typing import Dict, List
import os, re

class MiniAgent:
    def __init__(self, llm: Myllm):
        self.llm = llm
        self.messages:List[Dict[str, str]]=[
            {
                "role": "system",
                "content":(
                    "你是一个助手。"
                    "如果用户的问题需要计算，请严格输出工具调用格式："
                    "[TOOL:calculator:表达式]。"
                    "如果不需要工具，就直接正常回答。"
                ),
            }
        ]
        
    def run(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        first_response = self.llm.think(self.messages)
        tool_call = self._parse_tool_call(first_response)

        if not tool_call:
            self.messages.append({"role": "assistant", "content": first_response})
            return first_response

        tool_name, tool_input = tool_call #解包
        tool_result = self._call_tool(tool_name, tool_input)

        self.messages.append({"role": "assistant", "content": first_response})
        self.messages.append(
            {
                "role": "user",
                "content": f"工具执行结果：{tool_result}。请基于这个结果回答用户问题。",
            }
        )

        final_response = self.llm.think(self.messages)
        self.messages.append({"role": "assistant", "content": final_response})
        return final_response
    
    def _parse_tool_call(self, text: str) -> tuple[str, str] | None:
        match = re.search(r"\[TOOL:(\w+):(.+?)\]", text)
        if not match:
            return None
        tool_name = match.group(1)
        tool_input = match.group(2)
        return tool_name, tool_input #打包成元组返回
        
        
    def _call_tool(self, name, input):
        if name=="calculator":
            return calcultor(input)
        return f"未知工具: {name}"