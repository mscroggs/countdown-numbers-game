# Run this file to print out all combinations that lead to all totals being possible

from itertools import combinations, combinations_with_replacement
from search import possible

ls = []
for i in range(1,11):
    ls.append(i)
    ls.append(i)
ls += [25,50,75,100]

for n in range(5):
    for large in combinations([25,50,75,100], n):
        for small in combinations_with_replacement(range(1,11), 6-n):
            try:
                assert max([len([s for s in small if s==i]) for i in range(1,11)])<=2
                made = possible(small+large)
                if len([m for m in made if m is None]) == 0:
                    print small+large
            except AssertionError:
                pass
                
