class students:
     college = "RGIT"
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks
          print("data had been added to database...!")


s1 = students("Vipul",97)
print(s1.name, s1.marks, s1.college)

s2 = students("Vajay",91)
print(s2.name, s2.marks, students.college)