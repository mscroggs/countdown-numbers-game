# Run this file to save a file showing how to make totals from the following numbers
numbers = [3,6,8,10,75,100]

from search import possible

def format(j):
    if j is None:
        return "-"
    return j

for numbers in [[5,6,8,9,10,100],
    [5,6,7,8,10,100],
    [4,6,7,8,9,100],
    [3,6,7,8,10,100],
    [3,5,7,8,9,100],
    [2,5,6,8,9,100],
    [2,6,7,8,9,100],
    [5,6,8,9,75,100],
    [3,6,8,10,75,100],
    [2,6,9,10,75,100]]:
    print numbers

    made = possible(numbers)

    with open("output/"+"-".join([str(i) for i in numbers])+".txt","w") as f:
        f.write("\n".join([str(i)+" "+format(j) for i,j in made.items()]))
