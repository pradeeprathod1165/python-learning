with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.")

with open("sample.txt", "r") as f:
    print(f.read())


#json example
import json

data = {"name": "Pradeep", "role": "Engineer"}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded)
