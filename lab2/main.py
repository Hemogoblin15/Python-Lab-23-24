# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def ex1(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    num1 = 0
    num2 = 1
    next_number = num2
    count = 1
    fibonacci = [0, 1]

    while count < n:
        fibonacci.append(next_number)
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return fibonacci


# print(ex1(5))


# 2 Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def ex2(numbers):
    return [i for i in numbers if len([y for y in range(2, i // 2 + 1) if i % y == 0]) == 0]


# print(ex2([2, 55, 10, 14, 23]))

# 3 Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def ex3(a, b):
    intersection = list(set(a).intersection(b))
    union = list(set(a).union(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a


# print(ex3([1,2,3,4,5], [3,4,5,6,7]))

# 4 Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer).
# The function will return the song composed by going through the musical notes beginning with
# the start position and following the moves given as parameter.
# compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# will return ["mi", "fa", "do", "sol", "re"]

def ex4(notes, moves, start_position):
    position = start_position
    song = [notes[(position := (position + move) % len(notes))] for move in moves]
    return [notes[start_position]] + song


# print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# 5. Write a function that receives as parameter a matrix and will return the matrix
# obtained by replacing all the elements under the main diagonal with 0 (zero).

def ex5(matrix):
    return [[matrix[i][j] if i <= j else 0 for j in range(len(matrix[i]))] for i in range(len(matrix))]


# print(ex5([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2
# lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def ex6(*args):
    total_list = []
    for arg in args[:-1]:
        total_list += arg
    x = args[-1]
    aux = set()
    for i in total_list:
        if total_list.count(i) == x:
            aux.add(i)
    return list(aux)


# print(ex6([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], 2))

# 7. Write a function that receives as parameter a list of numbers (integers)
# and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list
# and the second element will be the greatest palindrome number.

def ex7(numbers):
    is_palindrome = lambda x: True if str(x) == (str(x)[::-1]) else False
    palindromes = [i for i in numbers if is_palindrome(i)]
    return len(palindromes), max(palindromes)


# print(ex7([121, 123, 337733]))

def create_condition_lambda(x, flag):
    if flag:
        return lambda i: i % x == 0
    return lambda i: i % x != 0


def ex8(strings, x=1, flag=True):
    condition = create_condition_lambda(x, flag)
    return list(map(lambda string: [letter for letter in string if condition(ord(letter))], strings))

# print(ex8(["test", "hello", "lab002"], 2, False))

    # 9. Write a function that receives as parameter a matrix which represents the heights of the spectators
    # in a stadium and will return a list of tuples (line, column) each one representing
    # a seat of a spectator which can't see the game.
    # A spectator can't see the game if there is at least one taller spectator standing in front of him.
    # All the seats are occupied. All the seats are at the same level.
    # Row and column indexing starts from 0, beginning with the closest row from the field. Example:
    # FIELD
    # [[1, 2, 3, 2, 1, 1],
    #  [2, 4, 4, 3, 7, 2],
    #  [5, 5, 2, 5, 6, 4],
    #  [6, 6, 7, 6, 7, 5]]

    # Will return : [(2, 2), (3, 4), (2, 4)]


def ex9(matrix):
    result = []
    matrix = list(zip(*matrix))
    maxim = 0
    for indexR, row in enumerate(matrix):
        for indexC, column in enumerate(row):
            if column > maxim:
                maxim = column
            else:
                result.append((indexC, indexR))
        maxim = 0
    return result


# print(
#     ex9([[1, 2, 3, 2, 1, 1],
#          [2, 4, 4, 3, 7, 2],
#          [5, 5, 2, 5, 6, 4],
#          [6, 6, 7, 6, 7, 5]
#          ]))

# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items
# on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"]
# return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def ex10(*args):
    return list(zip(*args))


# print(ex10([1,2,3], [5,7], ["a", "b"], [10, 11, 12] ))
# print(ex10( [1,2,3], [5,6,7], ["a", "b", "c"]))

# 11. Write a function that will order a list of string tuples
# based on the 3rd character of the 2nd element in the tuple. Example:
# ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc',  'bcd')]

def ex11(tuples):
    return sorted(tuples, key=lambda x: x[1][2])


# print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

def ex12(words):
    rhymes = {}
    for word in words:
        if word[-2:] not in rhymes.keys():
            rhymes[word[-2:]] = [word]
        else:
            rhymes[word[-2:]] += [word]
    return [i for i in rhymes.values()]


print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))
