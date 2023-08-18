word = input("Give me a word:")

word_in = list(reversed(word))
#print(word_in)

if word_in == list(word) :
    print ("The word %s is a palindrome" % word)
else:
    print ("The word %s is not a palindrome" % word)