import pytest

words = ["Python", "AEIOUY", "bcd", "", "Próba żółwia"]
vovels = "aeiouóyąęAEIOUÓYĄĘ"
def vovels_test(words):
    for word in words:
        licznik = 0
        for letter in word:
            if letter in vovels:
                licznik += 1
            else:
                licznik +=0
        print(f"Liczba samogłosek w {word}: {licznik}")