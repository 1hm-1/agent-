import os
from typing import Dict, List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class Myllm:
    def __init__(self, 
                 model:str=None, 
                 api_key: str=None, 
                 base_url: str=None, 
                 timeout:int=None):
        self.model = model or os.getenv("MODEL")
        api_key = api_key or os.getenv("API_KEY")
        base_url = base_url or os.getenv("BASE_URL")
        timeout = timeout or int(os.getenv("TIME_OUT") or 60) 
        
        if not api_key:
            raise ValueError("api key没有正确配置")
        
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
    def think(self, msgs:List[Dict[str, str]], temperature:float=0):
        print(f"-----------thinking with {self.model}------------")
        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages = msgs,
                temperature = temperature,
                stream = False
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during API call: {e}")
            return None
            
            