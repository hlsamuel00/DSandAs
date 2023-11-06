# Given two crystal balls that will break if dropped from a high enough distance, determine the exact spot in which it will break in the most optimized way. 


def two_crystal_balls(breaks: list[bool]) -> int:
    jump_amount = int(len(breaks) ** .5)

    for idx in range(jump_amount, len(breaks), jump_amount):
        if breaks[idx]: break

    idx -= jump_amount
    for _ in range(0, jump_amount):
        if breaks[idx]: return idx
        idx += 1
    
    return -1


two_crystals_test = [False, False, False, False, False, False, False, False, False, False]
print(two_crystal_balls(two_crystals_test))