def counter(start):

    def inc1(step=1):
        nonlocal start
        start += step
        # print(start)
        return start
    
    def inc2(step=1):
        nonlocal start
        start += step
        # print(start)
        return start
    
    return inc1, inc2


my_inc, another_inc = counter(5)

print(my_inc())
print(my_inc())
print(my_inc())
print(another_inc())
print(another_inc())
print(my_inc())
