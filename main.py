def flat_generator(lst):
    cursor = 0
    cursor2 = 0
    while cursor < len(lst):
        data = lst[cursor][cursor2]
        yield data
        cursor2 += 1
        if cursor2 >= len(lst[cursor]):
            cursor += 1
            cursor2 = 0

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)