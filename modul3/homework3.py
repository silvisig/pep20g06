def ordered_ints(list_of_objects: list):
    new_list = []
    for i in list_of_objects:
        if i == ():
            new_list.append(int(len(i)))
        else:
            new_list.append(int(i))
    new_list.sort(reverse=True)
    return new_list


print(ordered_ints([1, True, '123', False, 6, ()]))
def sum_of_square(n: int):
    if n == 0:
        return 0
    else:
        return n ** 2 + sum_of_square(n - 1)


print(sum_of_square(10))
def factorial_of_squares(n: int):
    if n == 1:
        return 1
    else:
        return n ** 2 * factorial_of_squares(n - 1)


print(factorial_of_squares(3))
def process_text(text: str):
    first_text = ""
    # second_text = ""
    for i in text:
        if i == " ":
            split_text = text.split(" ", 1)[0]
            first_text = split_text.upper()
            second_text = text.split(" ", 1)[1]

            for i in second_text:
                if (i != i.lower()) or (i == " ") or (i == i.isnumeric()):
                    second_text = second_text.replace(i, '_')

    return (first_text, second_text)


print(process_text('1234567a Text to te5t'))