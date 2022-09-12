print("\t\t\tWELCOME TO THE BREAKFAST PORTAL")
print("\t\t\t=================================")
import mysql.connector as ms
cn=ms.connect(host='localhost',username='root',passwd='',database='club')
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
    print("\n\n")
cr.execute("select * from breakfast")
for i in cr:
    print("The breakfast For Monday Is:- \t\t",i[0])
    print("The breakfast For Tuesday Is:-\t\t",i[1])
    print("The breakfast For Wensday Is:-\t\t",i[2])
    print("The breakfast For Thrusday Is:-\t\t",i[3])
    print("The breakfast For Friday Is:-\t\t",i[4])
    print("The breakfast For Satday Is:-\t\t",i[5])
    print("The breakfast For Sunday Is:-\t\t",i[6])
