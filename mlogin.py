import mysql.connector as ms
cn=ms.connect(host='localhost',username='root',passwd='',database='club')
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
print("PLEASE QUOTE THE NAME AND PASSWORD WITHIN INVERTED COMMAS")
u=input("Enter the username:- ")
pas=input("Enter the passward:- ")

print("PRESS Y TO PROCEED ")
Y=input("\t\t")

while Y=='y' or Y=='Y':
    print("\t\t\t    WELCOME TO MEMBERS PORTAL  ")
    print("\t\t\t    *********************************  ")
    print("\t\t1:To display the latest events in the club ")
    print("\t\t---------------------------------------------------------------")
    print("\t\t2:To display your records ")
    print("\t\t-------------------------------------------")
    print("\t\t3:To display the sports facilities")
    print("\t\t-----------------------------------------------------")
    print("\t\t4:To display food facilities ")
    print("\t\t---------------------------------------------")
    print("\t\t5:To display Hotel facilities")
    print("\t\t---------------------------------------------") 
    print("\t\t6:Nutritionist")
    print("\t\t----------------------")
    print("\t\t7:User's Feedback")
    print("\t\t------------------------------")
    print("\t\t8:Exit")
    print("\t\t----------")

    choice=int(input("ENTER YOUR CHOICE:- "))
    if choice==1:
        print("WELCOME TO THE EVENTS PORTAL")
        print("1:To Display The Events To Be Conducted For Families")
        print("2:To Display The Events To Be Conducted For Ladies")
        print("3:To Display The Events To Be Conducted For Gents")
        print("4:To Display The Events To Be Conducted For Children")
        x=int(input("Enter Your Choice:"))
        if x==1:
            print("The Functions Available For Families are:-")
            print("1.Birthday Party")
            print("2.Retirement Party")
            print("3.Engagement Parties")
            print("4.Get Together Parties")
            print("5.Dandia Parties")
            z=int(input("Enter your choice"))
            if z==1:
                print("\t\t\t BIRTHDAY PARTIES")
                c=15000
                print("The Total Cost Of Birthday Party Arrangement Is",c,"rupees") 
            elif z==2:
                print("\t\t\t RETIREMENT PARTIES")
                c=25000
                print("The Total Cost Of Retirement Party Arrangement Is",c,"rupees") 
            elif z==3:
                print("\t\t\t ENGAGEMENT PARTIES")
                c=30000
                print("The Total Cost Of Engagement Party Arrangement Is",c,"rupees") 
            elif z==4:
                print("\t\t\t GET TOGETHER PARTIES")
                c=18000
                print("The Total Cost Of Get Together Party Arrangement Is",c,"rupees") 
            elif z==5:
                print("\t\t\t DANDIA PARTIES")
                c=40000
                print("The Total Cost Of Dandia Party Arrangement Is",c,"rupees") 

        elif x==2:
            print("The Functions Available For Ladies are:-")
            print("1.kitty Party")
            print("2.Religious Functions")
            print("3.Personal Parties")
            print("4.Get Together Parties")
            print("5.Yoga Samiti(females)")
            z=int(input("Enter your choice"))
            if z==1:
                print("\t\t\t KITTY PARTIES")
                c=15000
                print("The Total Cost Of Birthday Party Arrangement Is",c,"rupees") 
            elif z==2:
                print("\t\t\t RELIGIOUS PARTIES")
                c=25000
                print("The Total Cost Of Retirement Party Arrangement Is",c,"rupees") 
            elif z==3:
                print("\t\t\t PERSONAL PARTIES")
                c=35000
                print("The Total Cost Of Engagement Party Arrangement Is",c,"rupees") 
            elif z==4:
                print("\t\t\t GET TOGETHER PARTIES")
                c=25000
                print("The Total Cost Of Get Together Party Arrangement Is",c,"rupees") 
            elif z==5:
                print("\t\t\t YOGA-SAMITI")
                c=45000
                print("The Total Cost Of Dandia Party Arrangement Is",c,"rupees") 

        elif x==3:
            print("The Functions Available For Gents are:-")
            print("1.Birthday Party")
            print("2.Retirement Party")
            print("3.Success Parties")
            print("4.Sports Events")
            print("5.Yoga Samiti(males)")
            z=int(input("Enter your choice"))
            if z==1:
                print("\t\t\t BIRTHDAY PARTIES")
                c=15000
                print("The Total Cost Of Birthday Party Arrangement Is",c,"rupees") 
            elif z==2:
                print("\t\t\t RETIREMENT PARTIES")
                c=15000
                print("The Total Cost Of Retirement Party Arrangement Is",c,"rupees") 
            elif z==3:
                print("\t\t\t SUCCESS PARTIES")
                c=15000
                print("The Total Cost Of Success Party Arrangement Is",c,"rupees") 
            elif z==4:
                print("\t\t\t SPORTS EVENTS")
                c=15000
                print("The Total Cost Of Sports Events Arrangement Is",c,"rupees") 
            elif z==5:
                print("\t\t\t YOGA-SAMITI")
                c=15000
                print("The Total Yoga Samiti Arrangement Is",c,"rupees") 

        elif x==4:
            print("The Functions Available For Children are:-")
            print("1.Birthday Party")
            print("2.Farewell Party")
            print("3.After Exam Parties")
            print("4.Sports Events")
            z=int(input("Enter your choice"))
            if z==1:
                print("\t\t\t BIRTHDAY PARTIES")
                c=15000
                print("The Total Cost Of Birthday Party Arrangement Is",c,"rupees") 
            elif z==2:
                print("\t\t\t FAREWELL PARTIES")
                c=45000
                print("The Total Cost Of Farewell Party Arrangement Is",c,"rupees") 
            elif z==3:
                print("\t\t\t AFTER-EXAM PARTIES")
                c=20000
                print("The Total Cost Of After Exam Party Arrangement Is",c,"rupees") 
            elif z==4:
                print("\t\t\t SPORTS EVENTS")
                c=18000
                print("The Total Cost Of Sports Events Arrangement Is",c,"rupees") 

    elif choice==2:
        cr.execute("select * from registration where  passward={}".format(pas))
        for i in cr:
          print(i)
          print("Member Number is:-",i[0])
          print("Member Name is:-   ",i[1])
          print("Country is:-              ",i[2])
          print("State is:-                  ",i[3])
          print("City is:-                     ",i[4])
          print("Phone Number is:-   ",i[5])
          print("email-id is:-              ",i[6])
          print("password is:-           ",i[7])

    elif choice==3:
        import sports
                    
    elif choice==4:
        print("WELCOME TO THE FOOD PORTAL")
        print("============================")
        print("\t\t 1. Vegetarian")
        print("\t\t 2. Non-Vegetarian")
        ch=int(input("Enter your choice:- "))
        if ch==1:
            print("\t\t\t Welcome to Vegetarian's Portal")
            print("````````````````````````````````````````````````````")
            print("1. To display the Breakfast menu")
            print("2. To display the Lunch menu")
            print("3. To display the Dinner menu")
            a=int(input("Enter your choice:- "))
            if a==1:
                import breakfast
            elif a==2:
                import lunch
            elif a==3:
                import dinner
            
        elif ch==2:
            print("Welcome to Non-Vegetarian's Portal")
            print("````````````````````````````````````````````````````")
            print("1. To display the Breakfast menu")
            print("2. To display the Lunch menu")
            print("2. To display the Dinner menu")
            a=int(input("Enter your choice:- "))
            if a==1:
                import nbreakfast
            elif a==2:
                import nlunch
            elif a==3:
                import ndinner

    elif choice==5:
        print("\t\t\tWELCOME TO THE HOTEL FACILITIES")
        print("\t\t\t================================")
        print("1.To Display The Details Of The Party Halls")
        print("2.To Display The Details Of The Luxury rooms")
        print("3.To Display The Details Of The AC rooms")
        print("4.To Display The Details Of The Non-AC rooms")
        c=int(input("Enter Your Choice:-"))
        if c==1:
            print("THE PARTY HALLS ARE :-")
            print("1.BIG PARTY HALL(81 X 43 X 13)ft")
            print("2.SMALL PARTY HALL(46 X 24 X 10)ft")
            p=int(input("Enter your choice for halls:-"))
            if p==1:
                a=60000
                print("The Big Hall Details Are As Follows:-")
                print("The cost of the Complete Hall for one Day is",a," Rupees")
                import random
                try:
                    Member_no=random.randint(1,1000)
                    print("Your member number is:- ",Member_no) 
                    print("user_name:-")
                    user_nam=input("\t  ")
                    print("Phone_no:-")
                    phone_no=input("\t  ")
                    if len(phone_no)==10:
                        pass
                    else:
                        print("invalid entry")
                    print("Email_id:-")
                    email_id=input("\t ")
                    if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                        pass
                    else:
                        print("invalid email_id ")
                        print("Try Again!!")
                        print("Email_id:-")
                        email_id=input("\t ")
                        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                            pass
                        else:
                            print("INVALID EMAIL-ID")
                    r="insert into bhregistration values('%s','%s','%s','%s')" %(Member_no,user_nam,phone_no,email_id)
                    cr.execute(r)
                    cn.commit()
                except:
                    print("This Member Number Already Exist")
                    print("PLEASE TRY Again")
                cn.close()
                print("Thanks For Your Visit Sir/Madam")

            elif p==2:
                a=40000
                print("The Small Hall Details Are As Follows:-")
                print("The cost of the Complete Hall for one Day is",a," Rupees")
                import random
                try:
                    Member_no=random.randint(1,1000)
                    print("Your member number is:- ",Member_no) 
                    print("user_name:-")
                    user_nam=input("\t  ")
                    print("Phone_no:-")
                    phone_no=input("\t  ")
                    if len(phone_no)==10:
                        pass
                    else:
                        print("invalid entry")
                    print("Email_id:-")
                    email_id=input("\t ")
                    if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                        pass
                    else:
                        print("invalid email_id ")
                        print("Try Again!!")
                        print("Email_id:-")
                        email_id=input("\t ")
                        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                            pass
                        else:
                            print("INVALID EMAIL-ID")
                    r="insert into shregistration values('%s','%s','%s','%s')" %(Member_no,user_nam,phone_no,email_id)
                    cr.execute(r)
                    cn.commit()
                except:
                    print("This Member Number Already Exist")
                    print("PLEASE TRY Again")
                cn.close()

        elif c==2:
            a=3500
            print("The Luxury Room Details Are As Follows:-")
            print("The cost of the Luxury room for one Day is",a," Rupees")
            print("1.TO REGISTER FOR LUXURY ROOM")
            print("2.To EXIT FROM THIS PORTAL")
            choi=int(input("ENTER YOUR CHOICE:-"))
            if choi==1:
                    import random
                    try:
                        Member_no=random.randint(1,1000)
                        print("Your member number is:- ",Member_no) 
                        print("user_name:-")
                        user_nam=input("\t  ")
                        print("Phone_no:-")
                        phone_no=input("\t  ")
                        if len(phone_no)==10:
                            pass
                        else:
                            print("invalid entry")
                        print("Email_id:-")
                        email_id=input("\t ")
                        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                            pass
                        else:
                            print("invalid email_id ")
                            print("Try Again!!")
                            print("Email_id:-")
                            email_id=input("\t ")
                            if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                                pass
                            else:
                                print("INVALID EMAIL-ID")
                        r="insert into lrregistration values('%s','%s','%s','%s')" %(Member_no,user_nam,phone_no,email_id)
                        cr.execute(r)
                        cn.commit()
                    except:
                        print("This Member Number Already Exist")
                        print("PLEASE TRY Again")
                    cn.close()
            elif choi==2:
                break
        elif c==3:
            a=2000
            print("The AC Room Details Are As Follows:-")
            print("The cost of the AC Room for one Day is",a," Rupees")
            print("1.TO REGISTER FOR AC ROOM")
            print("2.To EXIT FROM THIS PORTAL")
            choi=int(input("ENTER YOUR CHOICE:-"))
            if choi==1:
                    import random
                    try:
                        Member_no=random.randint(1,1000)
                        print("Your member number is:- ",Member_no) 
                        print("user_name:-")
                        user_nam=input("\t  ")
                        print("Phone_no:-")
                        phone_no=input("\t  ")
                        if len(phone_no)==10:
                            pass
                        else:
                            print("invalid entry")
                        print("Email_id:-")
                        email_id=input("\t ")
                        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                            pass
                        else:
                            print("invalid email_id ")
                            print("Try Again!!")
                            print("Email_id:-")
                            email_id=input("\t ")
                            if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                                pass
                            else:
                                print("INVALID EMAIL-ID")
                        r="insert into acregistration values('%s','%s','%s','%s')" %(Member_no,user_nam,phone_no,email_id)
                        cr.execute(r)
                        cn.commit()
                    except:
                        print("This Member Number Already Exist")
                        print("PLEASE TRY Again")
                    cn.close()
            elif choi==2:
                break
                

        elif c==4:
            a=1700
            print("The Non-AC Room Details Are As Follows:-")
            print("The cost of the Non-AC Room for one Day is",a," Rupees")
            print("1.TO REGISTER NON-AC ROOM")
            print("2.To EXIT FROM THIS PORTAL")
            choi=int(input("ENTER YOUR CHOICE:-"))
            if choi==1:
                    import random
                    try:
                        Member_no=random.randint(1,1000)
                        print("Your member number is:- ",Member_no) 
                        print("user_name:-")
                        user_nam=input("\t  ")
                        print("Phone_no:-")
                        phone_no=input("\t  ")
                        if len(phone_no)==10:
                            pass
                        else:
                            print("invalid entry")
                        print("Email_id:-")
                        email_id=input("\t ")
                        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                            pass
                        else:
                            print("invalid email_id ")
                            print("Try Again!!")
                            print("Email_id:-")
                            email_id=input("\t ")
                            if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
                                pass
                            else:
                                print("INVALID EMAIL-ID")
                        r="insert into nacregistration values('%s','%s','%s','%s')" %(Member_no,user_nam,phone_no,email_id)
                        cr.execute(r)
                        cn.commit()
                    except:
                        print("This Member Number Already Exist")
                        print("PLEASE TRY Again")
                    cn.close()
            elif choi==2:
                break

        else:
            break
    elif choice==6:
        print("\t\t\t WELCOME TO THE NUTRITIONIST PORTAL")
        print("\t\t\t ====================================")
        print("\t\t\t")
        print("=========================================================================================")
        print("1.To Calculate Your BMI(Body Mass Index)")
        print("2.To Calculate Your CBD Dosage Calculator")
        print("3.To Calculate Your BMR(Basal Metabolic Rate) ")
        print("4.To Calculate Your Blood Alcohol Content ")
        print("5.To Calculate Your Body Fat")
        c=int(input("Enter Your Choice:- "))
        if c==1:
            print("Enter Your Height(meters):- ")
            h=int(input("\t\t"))
            print("Enter Your Weight(in kilo grams):- ")
            w=int(input("\t\t"))
            bmi=(w/(h**2))
            print(bmi)
            if (bmi >= 25.0):
                print("You are Over Weight")
            elif (bmi>=18.4) and (bmi<=24.9):
                print("You Are Completly Healthy")
            elif (bmi<18.4):
                print("You Are Under Nourished")
        elif c==2:
            print("Enter Your Species(Human/Animal):- ")
            s=input("\t\t")
            print("Enter Your Gender(Male/female):- ")
            g=input("\t\t")
            print("Enter Your Age:- ")
            a=int(input("\t\t"))
            print("Enter Your Height(in meteres):- ")
            h=int(input("\t\t"))
            print("Enter Your weight(in kilograms):- ")
            w=int(input("\t\t"))
            print("Enter Your Pain Level(Mild/Medium/Severe):- ")
            p=input("\t\t")
            bmi=(w/((h**2)))
            print("Your BMI is:-",bmi)
            if bmi>=16 and bmi<=18.5:
                ds=1
                print("Desired Strength=",ds,"mg each 4/5 kg")
                cbd=[w/(4.5)]*ds
                print("Your CBD Dosage is:-",cbd)
            elif bmi>18.5 and bmi<25:
                ds=3
                print("Desired Strength=",ds,"mg each 4/5 kg")
                cbd=[w/(4.5)]*ds
                print("Your CBD Dosage is:-",cbd) 
            elif bmi>=25 and bmi<=30:
                ds=6
                print("Desired Strength=",ds,"mg each 4/5 kg")
                cbd=[w/(4.5)]*ds
                print("Your CBD Dosage is:-",cbd)
        elif c==3:
            print("Enter Your Gender(Male/female):- ")
            g=input("\t\t")
            print("Enter Your Age:- ")
            a=int(input("\t\t"))
            print("Enter Your Height(in meteres):- ")
            h=int(input("\t\t"))
            print("Enter Your weight(in kilograms):- ")
            w=int(input("\t\t"))
            if (g=="MALE" or g=="male" or g=="Male"):
                s=5
                bmr=(10*w)+(6.25*h)-(5*a)+s
                print(bmr)
            elif(g=="FEMALE" or g=="female" or g=="Female"):
                s=161
                bmr=(10*w)+(6.25*h)-(5*a)-s
                print("The Basal Metabolic Rate is:-",bmr)
            else:
                print("INVALID CHOICE")
        elif c==4:
            print("Enter Your Gender(Male/female):- ")
            g=input("\t\t")
            print("Enter The Ounces Of Alcohol Consumed:- ")
            a=int(input("\t\t"))
            print("Enter The Hours Elapsed Since Drinking:- ")
            hr=int(input("\t\t"))
            print("Enter Your weight(in kilograms):- ")
            w=int(input("\t\t"))
            if (g=="MALE" or g=="male" or g=="Male"):
                r=0.73
                bac=[((a*5.14)/(w*r))-(0.015*hr)]
                print("The Body A lcohol Content is:-",bac)
            elif(g=="FEMALE" or g=="female" or g=="Female"):
                r=0.66
                bac=[((a*5.14)/(w*r))-(0.015*hr)]
                print("The Body A lcohol Content is:-",bac)
            else:
                print("INVALID CHOICE")
        elif c==5:
            print("Enter Your Age:- ")
            a=int(input("\t\t"))
            print("Enter Your Height(in meteres):- ")
            h=int(input("\t\t"))
            print("Enter Your weight(in kilograms):- ")
            w=int(input("\t\t"))
            print("Enter Your Gender(Male/female):- ")
            g=input("\t\t")

            bmi=(w/((h**2)))
            print("Your BMI is:-",bmi)
            if (g=="MALE" or g=="male" or g=="Male"):
                bf=(1.20*bmi)+(0.23*a)-16.2
                print("The Body Fat Percentage is:-",bf,"%")
            elif(g=="FEMALE" or g=="female" or g=="Female"):
                bf=(1.20*bmi)+(0.23*a)-5.4
                print("The Body Fat Percentage is:-",bf,"%")
            else:
                print("INVALID CHOICE")
            
            
    elif choice==7:
        print("Feedback")
        print("1.write reviews")
        print("2.read reviews")
        ch=int(input("Enter Your Choice if you want to read review or to write review:"))
        if ch==1:
            def feed():
                x=("\t\t"+"NAME "+"\t\t"+" RATINGS "+"\t\t\t"+"   REVIEWS ")
                y=("\n\t\t"+" ===== "+"\t\t"+" ======== "+"\t\t\t"+"   ======= ")
                rec=("\n\t\t"+n+"\t\t"+c+"\t\t\t"+a)
                f.write(rec)
                #f.write(x)
                #f.write(y)
                f.close()
                
            f=open("rating.txt","a+")
            n=input("Enter Your Name:-")
            a=input("Write Your Feedback:-")
            b=int(input("Give Ratings[1-5]:-"))
            if b==1:
                c="*"
                print()
                feed()
            elif b==2:
                c="* *"
                print()
                feed()
            elif b==3:
                c="* * *"
                print()
                feed()
            elif b==4:
                c="* * * *"
                print()
                feed()
            elif b==5:
                c="* * * * *"
                print()
                feed()
            else:
                print("Invalid Option")
                break
        elif ch==2:
            f=open("rating.txt","r")
            v=f.read()
            print(v)
            f.close()
    elif choice==8 :
        break
    else:
        print("\t\t\t\t You Entered An Invalid Option")
        print("\t\t\t\t\t TRY AGAIN")
        continue
