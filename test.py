# def test(f):
#     print("before ...")
#     f()
#     print("after ...")
#
#
# @test
# def func():
#     print("func was called")





class X(object):
    def __init__(self, a, b, range):
        self.a = a
        self.b = b
        self.range = range
    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('__call__ with （{}, {}）'.format(self.a, self.b))
    def __del__(self):
        print("!!!!!!!!!!!")
        del self.a
        del self.b
        del self.range

xInstance = X(1, 2, 3)
xInstance(3,4)
del xInstance