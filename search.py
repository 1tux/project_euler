from glob import glob


search = raw_input("Search? ")
for py_file in glob("*.py"):

	if search in open(py_file).read():
		print py_file