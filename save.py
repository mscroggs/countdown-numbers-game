# Run this file to save a file showing how to make totals from the following numbers
numbers = [3,6,8,10,75,100]

from search import possible

def format(j):
    if j is None:
        return "-"
    return j

made = possible(numbers)

with open("output/"+" ".join([str(i) for i in numbers]),"w") as f:
    f.write("\n".join([str(i)+" "+format(j) for i,j in made.items()]))
