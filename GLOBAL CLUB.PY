print("\n\n\t\t\t\t 🏫St.Joseph's Sr.Sec.School")
print("\t\t\t\t -----------------------------------------------")
print("\n\n\t\t\t       🕴   WELCOME TO GLOBAL CLUB's PORTAL  🕴")
print("\t\t\t     ================================")
print("\t\t\t                     वैश्विक क्लब में आपका स्वागत है ")
print("\t\t\t                     ====================")
print("\t\t\t                         عالمی کلب میں خوش آمدید")
print("\t\t\t                        ===============")
print("\n\tABOUT GLOBAL CLUB:- ")
print("\t````````````````````````````````````````")
print("\n\t\t The Global Club , Kanpur, is a dazzling destination to exchange your views.  ")
print("\t\t With premier hospitality, best in class services and captivating ambiance, ")
print("\t\t\t this venue promises you the remarkable guest experience")
print(" ")
print("\n\n\t President:  Mr. Surya Pratap Verma")
print("\t -----------------")
print("\t Vice-President:  Mr. Gaitonde Singh")
print("\t ------------------------")
print("\t\t\t\t\t\t\t\t Contact us on :- 6388730259")
print("\t\t 1.LOGIN {if staff}")
print("\t\t 2.LOGIN {if member}")
print("\t\t 3.REGISTER")
ch=int(input("\nENTER YOUR CHOICE►"))
print("`````````````````````````````````````")
if ch==1:
    print("Username:-")
    user=str(input("\t"))
    if user=='Surya Pratap Singh' or user=='SURYA PRATAP SINGH' or user=='surya pratap singh':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='president' or desig=='PRESIDENT' or desig=='President':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='surya123' or passward=='SURYA123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import president
    else:            
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")

    if user=='Gaitonde Singh' or user=='GAITONDE SINGH' or user=='gaitonde singh':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='vicepresident' or desig=='VICEPRESIDENT' or desig=='VicePresident':
            print("Passward►")
            passward=str(input("\t"))
            if passward=='gaitonde123' or passward=='GAITONDE123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import vicepresident
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")

    if user=='mukesh mehra' or user=='MUKESH MEHRA' or user=='Mukesh Mehra':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='treasurer' or desig=='TREASURER' or desig=='Treasurer':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='mukesh123' or passward=='MUKESH123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import treasurer
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")

    if user=='saurav sharma' or user=='SAURAV SHARMA' or user=='Saurav Sharma':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='event manager' or desig=='EVENT MANAGER' or desig=='Event Manager':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='saurav123' or passward=='SAURAV123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import emanager
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")

    if user=='manish pandey' or user=='MANISH PANDEY' or user=='Manish Pandey':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='sports manager' or desig=='SPORTS MANAGER' or desig=='Sports Manager':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='manish123' or passward=='MANISH123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import smanager
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")
    if user=='vinay chauhan' or user=='VINAY CHAUHAN' or user=='Vinay Chauhan':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='executive manager' or desig=='EXECUTIVE MANAGER' or desig=='Executive Manager':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='vinay123' or passward=='VINAY123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import executivemanager
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")
    if user=='Shoeb Khan' or user=='SHOEB KHAN' or user=='shoeb khan':
        print("DESIGNATION:-")
        desig=str(input("\t"))
        if desig=='executive manager' or desig=='EXECUTIVE MANAGER' or desig=='Executive Manager':
            print("Passward:-")
            passward=str(input("\t"))
            if passward=='shoeb123' or passward=='SHOEB123':
                print("\t\t\t\t֍ACCESS GRANTED֍")
                import executivemanager
    else:
        print("\t\t\t\tACCESS DENIED😞")
        print("\t\t\t\t TRY AGAIN !!")

if ch==2:
    print("***************************************************************************************************************")
    print("WELCOME TO MEMBER-LOGIN PANNEL")
    print("------------------------------------------------------------------")
    import mlogin   
 
if ch==3:
    print("***************************************************************************************************************")
    print("WELCOME TO REGISTRATION PANNEL")
    print("----------------------------------------------------------------")
    print("The Global Club provides the best facillities to our members.")
    import registration
   
        





