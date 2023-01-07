
prams = [1, 2]

inputs = [{1:'a', 2:'b'}, {1:'c', 2:'d'}, {1:'e'}, {2:'d'}]

for input in inputs:
    for pram in prams:
        if pram not in input:
            print(pram)


