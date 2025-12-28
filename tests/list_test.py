import pytest
def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

try:
    print(flatten_list([1, 2, 3]))
    print(flatten_list([1, [2, 3], [4, [5]]]))
    print(flatten_list([]))
    print(flatten_list([[[1]]]))
    print(flatten_list([[1, [2, [3, [4]]]]]))
finally:
    pass


