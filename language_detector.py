#obviously we import from some sort of language library
from langdetect import detect
text = input("Enter text in any language: ")
print(detect(text))

#this was the best module I could find, download first before use!