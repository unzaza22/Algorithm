from Stack import Stack


# input: str
# output: is_error : boolean
# output: location : int

def bracket_check(input_string):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(input_string)):
        s = input_string[i]
        if s in "([{":
            stack.push((s, i))
        elif s in ")]}":
            if not stack.isEmpty():
                p, loc = stack.pop()
                if not ((p == '(' and s == ')') or (p == '[' and s == ']') or (p == '{' and s == '}')):
                    is_error = True
                    location.append(i)


            else:
                is_error = True
                location.append(i)

    while not stack.isEmpty():
        _, loc = stack.pop()
        is_error = True
        location.append(loc)

    return is_error, sorted(location)


# test_string = '[{(Hello'
# isError, locations = bracket_check(test_string)
# print('Error: ', isError)
# print('Location: ', locations)