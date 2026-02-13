story=input("What is the story? ")
article=['a','an','the']
words=story.split()
filtered_words=[word for word in words if word.lower() not in article]
result=' '.join(filtered_words)
print(result)