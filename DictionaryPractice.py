#Count the occurrence of each vowel in the sentence given as input by the user.
vowel_count={"a":0,"e":0,"i":0,"o":0,"u":0}
sentence = input("Write a sentence")
for c in sentence:
    print(c)
    if c in vowel_count:
        vowel_count[c]=vowel_count[c]+1
print(vowel_count)
#Count the occurrence of each alphabet that occurs in the sentence given as input by the user.
letter_count={}
sentence_2= input("Write another sentence.").lower()
for c in sentence_2:
    if c.isalpha():
        if c not in letter_count:
            letter_count[c]=1
        else:
            letter_count[c]=letter_count[c]+1
print(letter_count)
#Find if a given number entered by the user is a pangram or not ?
#A pangram number is a number which contains at least one occurrence of each digit.
num_count={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
number=input("Write a number.")
for n in number:
    n=int(n)
    if n in num_count:
        num_count[n]=num_count[n]+1
if 0 in num_count.values():
    print("Your number is not a pangram")
else:
    print("Your number is a pangram")
