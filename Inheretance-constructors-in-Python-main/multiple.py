class A:
    varA = "Student is in class A"

class B:
    varB ="Student is in class B"

class C(A,B):
    varC ="Student is in class c"

p = C()
print(p.varA)
print(p.varB)
print(p.varC)