import math

def ex1():
    s = input()
    numbers = s.split(" ")
    numbers = list(map(lambda x: int(x), numbers))
    gcd = numbers[0]
    for number in numbers:
        gcd = math.gcd(gcd, number)
    print(gcd)


def ex2():
    s = input()
    counter = [s.count(x) for x in "aeiouAEIOU"]
    print(sum(counter))


def ex3():
    a = input()
    b = input()
    print(a.count(b))


def ex4():
    s = input()
    output = ""
    for char in s:
        if char == char.lower():
            output += char
        else:
            output += "_" + char.lower()
    print(output)


def ex5():
    matrix = [['f', 'i', 'r', 's'],
              ['n', '_', 'l', 't'],
              ['o', 'b', 'a', '_'],
              ['h', 't', 'y', 'p']]

    string = []
    while matrix:
        string += matrix[0]
        matrix = list(zip(*matrix[1:]))
        matrix.reverse()
    print(''.join(string))


def ex6():
    n = int(input())
    m = n
    c = 0
    while n:
        c = c * 10 + n % 10
        n = int(n / 10)

    if c == m:
        print(True)
        print(c, m)
    else:
        print(False)
        print(c, m)


def ex7():
    output = ""
    ok = 0
    s = input()
    for index in range(0, len(s)):
        while s[index] in "1234567890":
            ok = 1
            output += s[index]
            index += 1
            if index == len(s):
                break
        if (ok):
            break
    print(output)


def ex8():
    counter = 0
    number = int(input())
    binaru = bin(number)

    for char in binaru:
        if char == '1':
            counter += 1

    print(counter)

def ex9():
    string = input()
    string = string.lower()
    counter = {}

    for char in string:
        if char.isalpha():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

    maxim = max(counter, key=counter.get)
    print(maxim)

def ex10():
    string = input()
    string = string.lower()
    word_list = string.split(" ")
    words = {}

    for word in word_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(len(words))

ex10()