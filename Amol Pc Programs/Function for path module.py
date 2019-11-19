import os

join = os.path.join('amol', 'suryaanhi')
print(join)

split = os.path.split('amol')
print(split)

out = os.path.normpath("foo/./bar")
print(out)

abspath = os.path.abspath('python')
print(abspath)

exits = os.path.exists('amol')
print(exits)
