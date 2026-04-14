import os 

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
print("已读取到 API Key")

base_url = os.getenv("OPENAI_BASE_URL")



model = os.getenv("OPENAI_MODEL","gpt-3.5-turbo")
retry_count = os.getenv("RETRY", "3")
debug = os.getenv("DEBUG", "false").lower() == "true"
config = {
    "model": model,
    "retry_count": int(retry_count),
    "debug": debug
}