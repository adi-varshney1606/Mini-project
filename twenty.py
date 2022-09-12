import mysql.connector as ms
d=input("enter database:-  ")     #club
n=input("enter username:-  ")    #root
cn=ms.connect(host='localhost',username=n,passwd='',database=d)
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
print("WELCOME TO THE 2020 INVESTMENT PORTAL")
cr.execute("select sum(item_cost*item_stock) from badminton;")
for i in cr:
    print("The total expense for badminton is: ",i[0])
    d=int(i[0])
cr.execute("select sum(item_cost*item_stock) from cricket;")
for i in cr:
    print("The total expense for cricket is: ",i[0])
    e=int(i[0])
cr.execute("select sum(item_cost*item_stock) from football;")
for i in cr:
    print("The total expense for football is: ",i[0])
    f=int(i[0])
cr.execute("select sum(salary) from staff")
for i in cr:
    print("The Total salary of the staff is:-",i[0])
    c=int(i[0])
v=5000
print("The total electricity bill is",v,"rupees/Month")  
x=d+e+f+c+v
print("The total investment in 2020 is:-",x,"rupees")







          
