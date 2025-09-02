def foo():
    print('hi')

def bar():
    print('bar')
    foo()
    print('bar but now')

bar()
