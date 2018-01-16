from PyQt4 import QtCore

class wind1():


    def __init__(self, parent=None):
        w2 = wind2(self)
        self.test=0

    def go(self):
        w2.check()


    def foo(self,text):
        print(text)


class wind2():
    def __init__(self, instw1):
        self.w1 = instw1

    def check(self):
        self.w1.foo("tests")

    def bar(self):
        print("OMG")


if __name__ == '__main__':
    w1 = wind1()
    w2 = wind2(w1)
    w2.check()
