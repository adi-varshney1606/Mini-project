print("WELCOME TO THE DINNER PORTAL")
print("==============================")
import mysql.connector as ms
cn=ms.connect(host='localhost',username='root',passwd='',database='club')
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
    print("\n\n")
cr.execute("select * from dinner")
for i in cr:
    print("The dinner For Monday Is:- \t\t",i[0])
    print("The dinner For Tuesday Is:-\t\t",i[1])
    print("The dinner For Wensday Is:-\t\t",i[2])
    print("The dinner For Thrusday Is:-\t\t",i[3])
    print("The dinner For Friday Is:-\t\t",i[4])
    print("The dinner For Satday Is:-\t\t",i[5])
    print("The dinner For Sunday Is:-\t\t",i[6])

