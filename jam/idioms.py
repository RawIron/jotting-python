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


class CopyList():

    @staticmethod
    def use_constructor(x):
        return list(x)

    @staticmethod
    def use_copy(x):
        import copy
        return copy.copy(x)

    @staticmethod
    def use_deepcopy(x):
        import copy
        return copy.deepcopy(x)

    @staticmethod
    def use_idiom(x):
        ''' shallow copy of a list '''
        return x[:]


copy_list = CopyList.use_idiom


def get_static(cls):
    import inspect
    return inspect.getmembers(cls, predicate=inspect.isfunction)


def copy_list_impl():
    return dict(get_static(CopyList)).values()


def is_unique_list(x):
    return len(set(x)) == len(x)


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
    def use_in_place(x):
        for v in x.sort():
            pass

    for v in sorted(x):
        pass


def filter_list(x, f):
    """ filter list with a callable f(a) which returns bool """
    def use_filter(x, f):
        return filter(f, x)

    def use_iteration(x, f):
        result = []
        for n in x:
            if f(n):
                result.append(n)
        return result

    return [n for n in x if f(n)]


def map_list(x, f):
    """ map list with a callable f(a) """
    def use_map(x, f):
        return map(f, x)

    def use_iteration(x, f):
        result = []
        for n in x:
            result.append(f(n))
        return result

    return [f(n) for n in x]


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


def call_func_with_tuple(x, f):
    """
    f(a,b) == f(*(a,b))
    """
    if not isinstance(x, tuple):
        raise ValueError
    return f(*x)


def call_func_with_dict(x, f):
    """
    f(a,b) == f(**{'a': 2, 'b': 4})
    """
    if not isinstance(x, dict):
        raise ValueError
    return f(**x)


def create_hash_index_on_list(x):
    def use_default_dict(x):
        from collections import defaultdict
        hindex = defaultdict(list)

        for ix, key in enumerate(x):
            hindex[key].append(ix)
        return hindex

    return use_default_dict(x)


def convert_camel_to_underscore(str):
    import re
    pattern = re.compile(r'[A-Z][a-z]+')
    # make first character upper case
    str = str[0].upper() + str[1:]
    return "_".join([word.lower() for word in pattern.findall(str)])


def convert_underscore_to_camel():
    return "".join([word.capitalize() for word in str.split('_')])
