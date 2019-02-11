#!usr/bin/python
sentence = "I am your genetically engineered reckoning"
words = sentence.split()

backwords = words[::-1]
reversedsentence = " ".join(backwords)

print(reversedsentence)