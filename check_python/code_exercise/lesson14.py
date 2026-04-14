import requests

def call_api(payload):
    try:
        response = requests.post(
            "https://example.com/api",
            json=payload,
            timeout=30
        )
        response.raise_for_status()  # 检查请求是否成功
        print(response.status_code)
    except requests.RequestException as e:
        print("请求失败", e)
        
        
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
}
call_api(payload)