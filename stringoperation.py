#1. Indexing
text = "Python"
print(text[0])   # P  (first char)
print(text[-1])  # n  (last char)

#2. Slicing
text = "Python"
print(text[0:4])   # Pyth  (from 0 to 3)
print(text[:3])    # Pyt   (from start to 2)
print(text[2:])    # thon  (from 2 to end)
print(text[::-1])  # nohtyP (reverse string)

#3. Changing Case
text = "pYtHoN"
print(text.upper())   # PYTHON
print(text.lower())   # python
print(text.title())   # Python
print(text.capitalize())  # Python
print(text.swapcase())    # PyThOn