def ex1(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    difference_a_b = set_a.difference(set_b)
    difference_b_a = set_b.difference(set_a)

    result = [intersection, union, difference_a_b, difference_b_a]

    return result


# set_a = {1, 2, 3, 4, 5}
# set_b = {3, 4, 5, 6, 7}
# print(ex1(set_a, set_b))


def ex2(s):
    char_counter = {}

    for char in s:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter


# print(ex2("Ana has apples."))


def ex3(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if len(dict1) != len(dict2):
            return False

        keys1 = sorted(dict1.keys())
        keys2 = sorted(dict2.keys())

        if keys1 != keys2:
            return False

        for key in keys1:
            if not ex3(dict1[key], dict2[key]):
                return False
        return True

    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False

        for item1, item2 in zip(dict1, dict2):
            if not ex3(item1, item2):
                return False
        return True

    return dict1 == dict2


# dictionar1 = {'a': 1, 'b': [2, 3, {'c': 4}], 'd': {'e': [5, 6]}}
# dictionar2 = {'b': [2, 3, {'c': 4}], 'd': {'e': [5, 6]}, 'a': 1}
#
# print(ex3(dictionar1, dictionar2))


def ex4(tag, content, **attributes):
    deschid_tag = f"<{tag}"

    for key, value in attributes.items():
        deschid_tag += f' {key}="{value}"'
    deschid_tag += ">"

    inchid_tag = f"</{tag}"

    xml_element = f"{deschid_tag}{content}{inchid_tag}"

    return xml_element


# print(ex4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

def ex5(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False

        value = dictionary[key]

        if not value.startswith(prefix) or not value.endswith(suffix):
            return False

        if middle not in value[1:-1]:
            return False

    for key in dictionary:
        if key not in [rule[0] for rule in rules]:
            return False

    return True


# print(ex5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#           {"key1": "come inside, it's too cold out", "key3": "this is not valid",
#            "key2": "starting the middle of winter",
#            }))


def ex6(lista):
    unice = len(set(lista))
    duplicate = len(lista) - unice
    return unice, duplicate


# print(ex6([1, 2, 2, 3, 4, 4, 5, 6, 6, 6]))


def ex7(*args):
    result = {}
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            key = f"{args[i]} | {args[j]}"
            value = args[i] | args[j]
            result[key] = value

            key = f"{args[i]} & {args[j]}"
            value = args[i] & args[j]
            result[key] = value

            key = f"{args[i]} - {args[j]}"
            value = args[i] - args[j]
            result[key] = value

            key = f"{args[j]} - {args[i]}"
            value = args[j] - args[i]
            result[key] = value

    return result


# print(ex7({1, 2}, {2, 3}))


def ex8(mapping):
    visited = set()
    lista = []
    current_key = mapping["start"]

    while current_key not in visited:
        visited.add(current_key)
        lista.append(current_key)
        current_key = mapping[current_key]

    return lista


# print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


def ex9(*args, **keywords):
    return sum(arg in keywords.values() for arg in args)

# print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
