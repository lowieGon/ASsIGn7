print("JOHN LOUIE B GONZALES | BSCOE 1-1 \n")

sentence = str(input("Enter your sentence: "))

Input = sentence
NumVowel = 0
NumConsonant = 0
NumWords = 0 


for Vowel in Input:
    if Vowel in "AEIOUaeiou":
        NumVowel = NumVowel + 1

for Consonant in Input:
    if Consonant in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        NumConsonant = NumConsonant + 1

countSpace = " "
for count in Input:
    for NumSpace in countSpace:
        if count == NumSpace:
            NumWords = NumWords + 1
            

print(f"NUMBER OF WORDS: {NumWords + 1}")
print(f"NUMBER OF VOWELS: {NumVowel}")
print(f"NUMBER OF CONSONANTS: {NumConsonant}")
