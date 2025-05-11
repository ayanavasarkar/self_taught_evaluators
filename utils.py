from together import Together
from typing import Any, Dict, Iterable, List
import json

def call_together_ai(prompt, client) -> str:
    
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def together_ai_client():
    # if api_key is None:
    api_key = "e91db0f4e4e8f06c89b83783344fa2a2d6866325b846820c671d6d306faeaecd"
    client = Together(api_key=api_key)
    return client

def save_to_jsonl(data: List[Dict], filename: str, write_mode="w"):
    with open(filename, write_mode) as file:
        for item in data:
            json_str = json.dumps(item)
            file.write(json_str + "\n")

def save_pairs_as_jsonl(pairs, filename):
    with open(filename, 'w') as f:
        for pair in pairs:
            f.write(json.dumps(pair) + '\n')

def load_from_jsonl(file_name: str) -> List[dict]:
    def load_json_line(line: str, i: int, file_name: str):
        try:
            return json.loads(line)
        except:
            raise ValueError(f"Error in line {i+1}\n{line} of {file_name}")

    with open(file_name, "r", encoding="UTF-8") as f:
        data = [load_json_line(line, i, file_name) for i, line in enumerate(f)]
    return data

def load_instructions_from_jsonl(file_name: str) -> List[dict]:
    def load_json_line(line: str, i: int, file_name: str):
        try:
            return json.loads(line)['instruction']
        except:
            raise ValueError(f"Error in line {i+1}\n{line} of {file_name}")

    with open(file_name, "r", encoding="UTF-8") as f:
        data = [load_json_line(line, i, file_name) for i, line in enumerate(f)]
    return data
