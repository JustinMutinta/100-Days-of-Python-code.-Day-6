"""
Create function to get 2 words and to verify if all the letters in the first show up in the second
Get both words.
If length of words is different, then message shows up saying the length is different.
Then for loop to go through each letter from the first word into the second one.
"""
def letter_check(word1, word2):
    final_boolean = True
    if len(word1) == len(word2):
        for char in word1:
            if word2.__contains__(char):
                final_boolean = True
            else:
                final_boolean = False
                break
    else:
        final_boolean = False

    if final_boolean == True:
        print("The words match")
    else:
        print("The words do not match")


print("Welcome to the letter verifier.")
word1 = input("Kindly enter your first word: ")
word2 = input("Kindly enter your second word: ")

letter_check(word1, word2)