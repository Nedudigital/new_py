#a palindrome is a word that reads the same forward and backwards
#we wanna find palindrome words in the sentence
def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")
    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome
sentence = input("Enter your sentence: ")
print(palindrome(sentence))                