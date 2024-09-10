def counter(start):
    def inc(step=1):
        nonlocal start
        start += step
        # print(start)
        return start

    return inc

my_inc = counter(1)
print(my_inc(2))
print(my_inc(4))
print(my_inc(3))
print(my_inc())

# print(my_inc.__closure__)
# print(my_inc())
# print(my_inc.__closure__)
