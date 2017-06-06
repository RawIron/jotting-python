"""
www.testdome.com PATH

Write a function that provides change directory (cd) function for an abstract file system.

Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
The function will not be passed any invalid paths.
Do not use built-in path-related functions.

For example:

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

should display '/a/b/c/x'.
"""


class PathString:
    ''' solve challenge with string operations only '''
    SEPARATOR = '/'

    @staticmethod
    def _is_absolute_path(path_str):
        return path_str.startswith(Path.SEPARATOR)

    @staticmethod
    def _is_in_subdir(path_str):
        return path_str != Path.SEPARATOR

    def __init__(self, path):
        self.current_path = path

    def cd(self, change_path):
        new_path = self.current_path

        if Path._is_absolute_path(change_path):
            change_path = change_path[1:]
            # wipe current path
            new_path = ""

        # /    + .. = /
        # /a   + .. = /
        # /a/b + .. = /a
        # /a   + b  = /a/b
        # /a   + /b = /b
        while change_path:
            pos = change_path.find(Path.SEPARATOR)
            if pos > 0:
                item = change_path[:pos]
                change_path = change_path[pos+1:]
            else:
                item = change_path
                change_path = ''

            if item == '..':
                if PathString._is_in_subdir(new_path):
                    del_pos = new_path.rfind(Path.SEPARATOR)
                    if del_pos > 0:
                        new_path = new_path[:del_pos]
                    elif del_pos == 0:
                        new_path = new_path[0]
            else:
                if new_path.endswith(Path.SEPARATOR):
                    new_path += item
                else:
                    new_path += Path.SEPARATOR + item

        self.current_path = new_path


class Path:
    SEPARATOR = '/'

    @staticmethod
    def _build_path_list(path_str):
        path_list = path_str.strip().split(Path.SEPARATOR)
        if Path._is_absolute_path(path_str):
            path_list = path_list[1:]
        return path_list

    @staticmethod
    def _build_path_string(path_list):
        return Path.SEPARATOR + Path.SEPARATOR.join(path_list)

    @staticmethod
    def _is_absolute_path(path_str):
        return path_str.startswith(Path.SEPARATOR)

    def __init__(self, path):
        self.current_path = path

    def cd(self, path):
        new_path = Path._build_path_list(self.current_path)

        change_path = Path._build_path_list(path)
        if Path._is_absolute_path(path):
            # wipe current path
            new_path = []

        # /    + .. = /
        # /a/b + .. = /a
        # /a   + b  = /a/b
        # /a   + /b = /b
        for item in change_path:
            if item == '..':
                del(new_path[-1:])
            else:
                new_path.append(item)
        self.current_path = Path._build_path_string(new_path)


if __name__ == "__main__":
    path = Path('/a/b/c/d')
    path.cd('../x')

    print(path.current_path)
