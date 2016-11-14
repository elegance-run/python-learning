import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**km):
            print('%s,%s():' %(text,func.__name__))
            return func(*args,**km)
        return wrapper
    return decorator

@log
def now():
    print('2016-11-10')

print(now())

@log('execute')
def now_1():
    print('2015-3-25')
print(now_1())