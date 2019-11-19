class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)


def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]


def count(lines):
    return len(lines)


ss = LineCounter("sample OSModules.py")
print(ss.read())

example_lines = read('sample OSModules.py')
lines_count = count(example_lines)
