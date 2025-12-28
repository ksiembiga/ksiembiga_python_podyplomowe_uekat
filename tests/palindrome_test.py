import pytest

words = ["kajak", "Kobyła ma mały bok", "python", "", "A"]
for word in words:
    word = word.lower()
    word = word.replace(" ", "")
    if word == word[::-1]:
        print(f'{word} True')
    else:
        print(f'{word} False')







