def pair_sum_seq(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total

def pair_sum(a,b):
    return a + b