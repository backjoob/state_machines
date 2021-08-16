class A:
    class B:
        msg = "B's message"
        def c(self):
            print(A.C.msg)
    class C:
        msg = "C's message"
        def b(self):
            print(A.B.msg)
b = A.B()
b.c()
c = A.C()
c.b()
