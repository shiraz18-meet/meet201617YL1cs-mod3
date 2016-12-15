from student import Student
shira=Student("Shira","Kfar Tavor","15","1.68","Cookies and Cream")
malak=Student("Malak","Nazareth","15","1.75","Chocolate")
eden=Student("Eden","Aloni Abba","15","1.60","Cookies and Cream")

shira.print_summary()
malak.print_summary()
eden.print_summary()
s=shira.get_giraffe_gap()
m=malak.get_giraffe_gap()
e=eden.get_giraffe_gap()
print(s,m,e)

