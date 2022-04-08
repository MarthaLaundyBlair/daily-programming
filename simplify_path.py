""""

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

. stay
.. go up one level

"""

def simplify_path(path):
    lst = path.split("/")
    print(lst)
    i = 0
    while i < len(lst):
        if lst[i] == ".":
            lst[i] = 0
        elif lst[i] == "..":
            print("hi")
            print(lst[i])
            lst[i] = 0
            lst[i-1] = 0
        i = i + 1

    lst = list(filter(lambda a: a != 0, lst))
    final_path = '/'.join(lst)

    return final_path


print(simplify_path("/usr/bin/../bin/./scripts/../"))