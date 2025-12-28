import pytest
import re
from collections import Counter

def frequencies_test(text) -> dict:
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return dict(Counter(words))
try:
    print(frequencies_test("To be or not to be"))
    print(frequencies_test("Hello, hello!"))
    print(frequencies_test(""))
    print(frequencies_test("Python Python python"))
    print(frequencies_test("Ala ma kota, a kot ma Ale."))
finally:
    pass
