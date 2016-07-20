# Run this file to print out all combinations that lead to all totals being possible

from itertools import combinations, combinations_with_replacement
from search import possible

ls = []
for i in range(1,11):
    ls.append(i)
    ls.append(i)
ls += [25,50,75,100]

count = 0

def format(stuff):
    stuff = str(stuff)
    return " "*(3-len(stuff)) + stuff

with open("output/countdown-combinations","w") as f:
    f.write("Numbers             Number of possible totals\n")

for n in range(5):
    for large in combinations([25,50,75,100], n):
        for small in combinations_with_replacement(range(1,11), 6-n):
            try:
                assert max([len([s for s in small if s==i]) for i in range(1,11)])<=2
                made = possible(small+large)
                strnum = " ".join([str(i) for i in small+large])
                possibles = len([m for m in made if made[m] is not None])
                with open("output/countdown-combinations","a") as f:
                    f.write(strnum + " "*(20-len(strnum)) + format(possibles)+"/899")
                    f.write("\n")
                if possibles == 899:
                    count += 0
                    print(small+large)
            except AssertionError:
                pass
            
print(str(count)+" combinations allow every total to be made")
