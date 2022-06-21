import pprint

def power(*numbers, p=2):
    return [(n ** p) for n in numbers]

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            break
    else:
        if x > 1:
            return True
    return False

def list_filter(items=None, option=0):
    """
    option:
        0 - to filter only even numbers
        1 - to filter only odd numbers
        2 - to filter prime numbers
    """
    if items == None or type(items) != type([]) or option not in [0, 1, 2]:
        return -1
    else:
        if option == 0:
            return list(filter(lambda x: not(x % 2), items))
        if option == 1:
            return list(filter(lambda x: x % 2, items))
        if option == 2:
            return list(filter(is_prime, items))

if __name__ == '__main__':
    pprint.PrettyPrinter(indent=2).pprint(power(0, 1, 2, 3, 4, 100, 20, 35, 11, p = 3))
    print(list_filter(items=[1, 2, 4, 5, 6, 3, 7, 17], option=2))
    print(list_filter(items=[1, 2, 4, 5, 6, 3, 7, 17], option=1))
    print(list_filter(items=[1, 2, 4, 5, 6, 3, 7, 17]))
    print(list_filter())
