class A():
    pass

class B():
    pass

class C(A,B):
    pass

c=C()


if __name__ == '__main__':
    if isinstance(c,B):
        print("ok")

