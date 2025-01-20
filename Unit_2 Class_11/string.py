sentence = "Essential for data cleaning, formatting, and user interactions."

# Split
print(sentence.split()) # for gaps
print(sentence.split(",")) # for comas
print(sentence.split("a"))

# replace
print(sentence.replace("data", "hello"))

# join(iterable)
print(sentence.join("123"))

# find(substring)
print(sentence.find("ziczac")) # -1 -> didn't find

# string slicing
text = "Python Programming"
print(text[7 : ])
print(text[4 : 10])
print(text[ : : 2])
print(text[ : : -1]) # reverse 
print(text[ : : -2]) # reverse 