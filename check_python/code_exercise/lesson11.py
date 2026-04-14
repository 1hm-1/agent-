import json

data  = {
    "model": "ds",
    "temperature": 0.1,
    "debug": None
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
for key, value in loaded_data.items():
    print(key, value)

messages = [{"name": "Alice", "age": 18},
            {"name": "Mike", "age": 12}]
with open("msg.json", "w", encoding="utf-8") as f:
    json.dump(messages,f, ensure_ascii=False, indent=2)


text = '{"name": "Alice","age": 18}'
data = json.loads(text)
print(data["name"])