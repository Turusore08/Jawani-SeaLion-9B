import json
from datasets import load_dataset

dataset = load_dataset("afrizalha/Gatra-2-Javanese", split="train")

dataset = dataset.shuffle(seed=42).select(range(20000,20100))

output_file = "gatra2_test.jsonl"

with open(output_file, "w", encoding="utf-8") as f:
    for row in dataset:
        chatml_format = {"messages": row["messages"]}
        f.write(json.dumps(chatml_format, ensure_ascii=False) + "\n")

print(f"Data tersimpan: {output_file}")