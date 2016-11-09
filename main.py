def num_producer():
    n=1
    while True:
        n=n+2
        yield n

def num_select(n):
    lambda x:x%n>0


def generator():
    yield 2
    g=generator()
    while True:
        n=next(g)
        yield n
        it=filter(num_select(n),it)

def main():
    for n in generator():
        if n<1000:
            print(n)
        else:
            break