from __future__ import division

def possible(numbers):
    made = {i:None for i in range(101,1000)}

    from itertools import permutations, product
    for nums in permutations([str(i) for i in numbers]):
        for signs in product(["+","-","/","*"], repeat=5):
            p = []
            p.append(nums[4]+signs[4]+nums[5])
            p.append(nums[3]+signs[3]+"("+nums[4]+signs[4]+nums[5]+")")
            p.append(nums[2]+signs[2]+"("+nums[3]+signs[3]+"("+nums[4]+signs[4]+nums[5]+"))")
            p.append(nums[1]+signs[1]+"("+nums[2]+signs[2]+"("+nums[3]+signs[3]+"("+nums[4]+signs[4]+nums[5]+")))")
            p.append(nums[0]+signs[0]+"("+nums[1]+signs[1]+"("+nums[2]+signs[2]+"("+nums[3]+signs[3]+"("+nums[4]+signs[4]+nums[5]+"))))")

            p.append("("+nums[2]+signs[2]+nums[3]+")"+signs[3]+"("+nums[4]+signs[4]+nums[5]+")")
            p.append(nums[1]+signs[1]+"(("+nums[2]+signs[2]+nums[3]+")"+signs[3]+"("+nums[4]+signs[4]+nums[5]+"))")
            p.append(nums[0]+signs[0]+"("+nums[1]+signs[1]+"(("+nums[2]+signs[2]+nums[3]+")"+signs[3]+"("+nums[4]+signs[4]+nums[5]+")))")

            p.append("("+nums[0]+signs[0]+nums[1]+")"+signs[1]+"(("+nums[2]+signs[2]+nums[3]+")"+signs[3]+"("+nums[4]+signs[4]+nums[5]+"))")

            for m in p:
                try:
                    e = eval(m)
                    if float(e).is_integer() and int(e) in made:
                        made[int(e)] = m
                except ZeroDivisionError:
                    pass
    return made
