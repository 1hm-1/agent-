from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

class HelloAgentsLLM:
    def __init__(self, model:str=None, api_key:str=None, base_url:str=None, timeout:int=None):
        self.model = model or os.getenv("MODEL_ID")
        api_key = api_key or os.getenv("API_KEY")
        base_url = base_url or os.getenv("BASE_URL")
        timeout = timeout or int(os.getenv("TIMEOUT") or 30)
        
        if not all([self.model, api_key, base_url]):
            raise ValueError("MODEL_ID, API_KEY, and BASE_URL must be set in environment variables or passed as arguments.")
        
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
        
    def think(self, messages: List[Dict[str, str]], temperature: float=0) -> str:
        print(f"Thinking with model: {self.model}")
        
        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages = messages,
                temperature = temperature,
                stream = True
            )
            print("✅ 大语言模型响应成功:")
            collected_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()  # 在流式输出结束后换行
            return "".join(collected_content)
        except Exception as e:
            print(f"Error during API call: {e}")
            return None
        
if __name__ == "__main__":
    try:
        llmclient = HelloAgentsLLM()
        
        example_messages = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code."},
            {"role": "user", "content": "写一个快速排序算法"}]
        
        print("——————————调用LLM——————————")
        
        responseText = llmclient.think(messages=example_messages)
        if responseText:
            print("\n\n--- 完整模型响应 ---")
            print("LLM Response:", responseText)
            
    except ValueError as e:
        print(f"Error initializing HelloAgentsLLM: {e}")
        