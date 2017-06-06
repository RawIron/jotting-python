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


class Path:
    SEPARATOR = '/'

    def __init__(self, path):
        self.current_path = path

    def _parse_path_string(self, path_str):
        return path_str.strip().split(Path.SEPARATOR)

    def _build_path_string(self, p):
        return Path.SEPARATOR.join([''] + p)

    def cd(self, new_path):
        current_path = self._parse_path_string(self.current_path)
        if current_path[0] == '':
            # remove root from absolute path
            current_path = current_path[1:]
        tmp_path = self._parse_path_string(new_path)

        # /    + .. = /
        # /a/b + .. = /a
        for item in tmp_path:
            if item == '..':
                del(current_path[-1:])
            else:
                current_path.append(item)
        self.current_path = self._build_path_string(current_path)
 

path = Path('/a/b/c/d')
path.cd('../x')

print(path.current_path)

