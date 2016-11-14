import functools

int_2=functools.partial(int,base=2)
print('10000=',int_2('10000'))
print('1000000=',int_2('1000000'))