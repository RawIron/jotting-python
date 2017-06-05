'''
python idioms
'''


def reverse_generator(x):
    '''
    generators can be infinite
    so this is an unsafe operation
    '''
    import types
    if not isinstance(x, types.GeneratorType):
        raise ValueError

    return reversed(list(x))


def reverse_string(str):
    def use_in_place(str):
        return reversed(str)

    return str[::-1]


def copy_list(x):
    def use_constructor(x):
        return list(x)

    def use_copy(x):
        import copy
        return copy.copy(x)

    def use_deepcopy(x):
        import copy
        return copy.deepcopy(x)

    return x[:]


def count_list(x):
    def use_reduce(x):
        return reduce(lambda acc, y: acc+1, x, 0)

    return len(x)


def count_value_in_list(x, value):
    def use_comprehension(x, value):
        return len([n for n in x if n == value])

    def use_map_reduce(x, value):
        return reduce(lambda x,y: x+1, filter(lambda y: y == value, x), 0)

    def use_iteration(x, value):
        count = 0
        for n in x:
            if n == value:
                count += 1
        return count

    return x.count(value)


def reverse_list(x):
    def use_in_place(x):
        return x.reverse()

    return x[::-1]


def iterate_list(x):
    for v in x:
        pass


def iterate_sorted_list(x):
    for v in sorted(x):
        pass


def iterate_dict(x):
    for k, v in x.iteritems():
        pass


def iterate_key_sorted_dict(x):
    for k, v in sorted(x.iteritems()):
        pass


def exchange_keys_with_duplicate_values_in_dict(x):
    '''
    new keys are the unique values
    new values are a list of keys
    '''
    def use_default_dict(x):
        from collections import defaultdict

        result = defaultdict(list)
        for key, value in x.items():
            result[value].append(key)
        return result

    def use_iteration(x):
        result = {}
        for key, value in x.items():
            if value in result:
                result[value].append(key)
            else:
                result[value] = [key]
        return result


def exchange_keys_with_unique_values_in_dict(x):
    '''
    keys and values are unique
    '''
    return dict((v,k) for k,v in x.iteritems())

