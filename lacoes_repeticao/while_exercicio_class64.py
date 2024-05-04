"""
Iterando strings com while
"""
#       01234567890.....
name = "Henrique Torres"
i = 0

while i <= len(name):
    print(f"{"*".join(name)}")
    i += 1