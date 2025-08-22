with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.")

with open("sample.txt", "r") as f:
    print(f.read())
