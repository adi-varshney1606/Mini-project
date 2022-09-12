print("WELCOME TO THE LUNCH PORTAL")
print("=============================")
import mysql.connector as ms
cn=ms.connect(host='localhost',username='root',passwd='',database='club')
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
    print("\n\n")
cr.execute("select * from nlunch")
for i in cr:
    print("The lunch For Monday Is:- \t\t",i[0])
    print("The lunch For Tuesday Is:-\t\t",i[1])
    print("The lunch For Wensday Is:-\t\t",i[2])
    print("The lunch For Thrusday Is:-\t\t",i[3])
    print("The lunch For Friday Is:-\t\t",i[4])
    print("The lunch For Satday Is:-\t\t",i[5])
    print("The lunch For Sunday Is:-\t\t",i[6])
