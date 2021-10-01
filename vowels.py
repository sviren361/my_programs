def vowel_find(string,vowel):
    final=[each for each in string if each in vowel]
    print(final)
    print(len(final))

string=input("Enter Sentence ")
vowel="AaEeIiOoUu"
vowel_find(string,vowel)