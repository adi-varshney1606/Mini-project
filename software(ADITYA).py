print("\t\t\t\t St.Joseph's Sr.Sec.School")
print("\t\t\t\t -------------------------------------------")
print("\t\t\t          WELCOME TO GLOBAL CLUB's PORTAL")
print("\n\tABOUT GLOBAL CLUB:- ")
print("\n\t\t The Global Club , Kanpur, is a dazzling destination to exchange your views.  ")
print("\t\t With premier hospitality, best in class services and captivating ambiance, ")
print("\t\t\t this venue promises you the remarkable guest experience")
print("\n\n\t President:  Mr. Surya Pratap Verma")
print("\t Vice-President:  Mr. Gaitonde Singh")
print("\n\n\t\t\t\t\t\t\t\t Contact us on :- 6388730259")
print("\tEnter your choice:")
print("\t\t ❶.LOGIN")
print("\t\t ❷.REGISTER")
ch=input("\nENTER YOUR CHOICE►")
if ch=='1':
    print("Username►")
    user=str(input("\t"))
    print("DESIGNATION►")
    desig=str(input("\t"))
    print("Passward►")
    passward=str(input("\t"))
    if passward=='glob12' or passward=='GLOB12':
        print("\t\t\t\t֍ACCESS GRANTED֍")

        if desig=='president' or desig=='PRESIDENT' or desig=='President':
            import mysql.connector as ms
            d=input("enter database:-  ")     #pop
            n=input("enter username:-  ")    #root
            cn=ms.connect(host='localhost',username=n,passwd='',database=d)
            if cn.is_connected():
                print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
                cr=cn.cursor()
                def add():
                    no=input("ENTER EMPLOYEE NO.")
                    na=input("ENTER EMPLOYEE NAME")
                    jo=input("ENTER DESIGNATION OF THE EMPLOY")
                    mg=input("ENTER THE mgr OF THE EMPLOYEE")
                    hire=input("ENTER THE DATE OF HIREING OF THE EMPLOYEE")
                    sa=input("ENTER THE SALARY OF THE EMPLOYEE")
                    com=input("ENTER THE COMMISSION OF THE EMPLOYEE")
                    dno=input("ENTER THE DEPARTMENT NO. OF THE EMPLOYEE")
                    cr.execute("insert into empl values(%d,%s,%s,%s,%y-%m-%d,%d,%d,%d)")
                    cn.close()
                def dis():
                    cr.execute("select * from empl") 
                    for i in cr:
                        print(i)
                def src():
                    no=input("ENTER THE EMPLOYEE NO. YOU WANT TO SEARCH:- ")
                    cr.execute("select * from empl where empno={}". format(no))
                    for i in cr:
                        print(i)
                def mod():
                    cr.execute("update empl set sal=sal+5000 where year(hiredate)>1991 and deptno=10")
                    print("total no of records updated=",cr.rowcount)

            while True:
                print("\t\t\t    WELCOME TO PRESIDENT's PORTAL")
                print("\t\t\t***********************************")
                print("\t\t❶:Add new records")
                print("\t\t-------------------------------")
                print("\t\t❷:Display all records")
                print("\t\t----------------------------------")
                print("\t\t❸:Search a record")
                print("\t\t-----------------------------")
                print("\t\t❹:Modify a record")
                print("\t\t----------------------------")
                print("\t\t❺:Exit from the program")
                print("\t\t---------------------------------------")
                choice=int(input("ENTER YOUR CHOICE:- "))
                if choice==1:
                    print("You have choosen to add new  records to the file")
                    print("=======================================")
                    print(add())               
                elif choice==2:
                    print("You have choosen to display all the records")
                    print("==================================")
                    print(dis())                  
                elif choice==3:
                    print("You have choosen to search the record")
                    print("===============================")
                    print(src())                
                elif choice==4:
                    print("You have choosen to modify the record")
                    print("================================")
                    print(mod())                
                elif choice==5:
                    print("H*O*P*E-Y*O*U-E*N*J*O*Y*E*D")
                    print("===========================")                         
                    break
        elif desig=='vicepresident' or desig=='VICEPRESIDENT' or desig=='VicePresident':
            import mysql.connector as ms
            d=input("enter database:-  ")     #pop
            n=input("enter username:-  ")    #root
            cn=ms.connect(host='localhost',username=n,passwd='',database=d)
            if cn.is_connected():
                print("\t\t          CONNECTION ESTABLISHED SUCCESSFULLY")
                cr=cn.cursor()
                def add():
                    no=input("ENTER EMPLOYEE NO.")
                    na=input("ENTER EMPLOYEE NAME")
                    jo=input("ENTER DESIGNATION OF THE EMPLOY")
                    mg=input("ENTER THE mgr OF THE EMPLOYEE")
                    hire=input("ENTER THE DATE OF HIREING OF THE EMPLOYEE")
                    sa=input("ENTER THE SALARY OF THE EMPLOYEE")
                    com=input("ENTER THE COMMISSION OF THE EMPLOYEE")
                    dno=input("ENTER THE DEPARTMENT NO. OF THE EMPLOYEE")
                    cr.execute("insert into empl values(%d,%s,%s,%s,%y-%m-%d,%d,%d,%d)")
                    cn.close()
                def dis():
                    cr.execute("select * from empl") 
                    for i in cr:
                        print(i)
                def src():
                    no=input("ENTER THE EMPLOYEE NO. YOU WANT TO SEARCH:- ")
                    cr.execute("select * from empl where empno={}". format(no))
                    for i in cr:
                        print(i)
                def mod():
                    cr.execute("update empl set sal=sal+5000 where year(hiredate)>1991 and deptno=10")
                    print("total no of records updated=",cr.rowcount)

            while True:
                print("\t\t  WELCOME TO VICE-PRESIDENT's PORTAL")
                print("\t\t\t***********************************")
                print("\t\t❶:Add new records")
                print("\t\t-------------------------------")
                print("\t\t❷:Display all records")
                print("\t\t----------------------------------")
                print("\t\t❸:Search a record")
                print("\t\t-----------------------------")
                print("\t\t❹:Modify a record")
                print("\t\t----------------------------")
                print("\t\t❺:Exit from the program")
                print("\t\t---------------------------------------")
                choice=int(input("ENTER YOUR CHOICE:- "))
                if choice==1:
                    print("You have choosen to add new  records to the file")
                    print("=======================================")
                    print(add())               
                elif choice==2:
                    print("You have choosen to display all the records")
                    print("==================================")
                    print(cr.execute("select * from empl"))                  
                elif choice==3:
                    print("You have choosen to search the record")
                    print("===============================")
                    print(src())                
                elif choice==4:
                    print("You have choosen to modify the record")
                    print("================================")
                    print(mod())                
                elif choice==5:
                    print("H*O*P*E-Y*O*U-E*N*J*O*Y*E*D")
                    print("===========================")                         
                    break

    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")
elif ch=='2':
    name=input("Enter Your Name:-  ")
    phno=str(input("Enter Your Phone No. :-  "))
    if phno.isdigit() and len(phno)==10:
        pass
    else:
        print(" invalid mobile number")
    address=input("Enter Your Address :- ") 
    email=str(input("Enter Your Mail Id :- "))
    if len(email)>7 and email[-10:]=='@gmail.com' or email[-10:]=='@yahoo.com':
        pass
    else:
        print("invalid")

