from django.http import HttpResponse
from django.shortcuts import render

from service.models import login1
from service.models import profilepatient

from django.core.mail import send_mail
from django.db import connection
from project import viewspatient as vp
import random

OTP = 0
log=""
pro=""
def index(request):
    return render(request,"home.html")

def signinn(request):
    return render(request,"signin.html")

def signin(request):
    n=""
    if request.method=="POST":
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        pas = login1.objects.raw("select id,password from service_login1 where email= %s", [emailid])
        if len(pas)==1:
            if password==pas[0].password:
               a = login1.objects.raw("select * from service_login1 where email = %s",[emailid])
               fname=a[0].fname
               lname=a[0].lname
               gender=a[0].gender
               if a[0].selectoption == "Patient":
                    vp.gain(emailid,fname,lname,gender)
                    b = profilepatient.objects.raw("select * from service_profilepatient where email = %s",[emailid])
                    print(b[0].bloodgroup)
                    print(b[0].phone)
                    print(b[0].dateofbirth)
                    print(b[0].address)
                    if (b[0].bloodgroup == None) or (b[0].phone == None) or (b[0].dateofbirth == None) or (b[0].address == None):
                        n="please fill all the profile details"
                        return render(request,"indexpatient.html",{'n':n})
                    else :
                         return render(request,"indexpatient.html")
                     
               else :#a[0].selectoption == "Doctor":
                   return render(request,index.html)
                    
                       
            else:
                 n="incorrect emil or password" 
        else:
            n="no such emilid found"
            return render(request,"signin.html",{'n':n})





def signup(request):
    return render(request,"signup.html")

def forget(request):
    return render(request,"froget_emil_otp.html")


def login(request):
    j=0
    global log
    n=""
    if request.method=="POST":
        selectoption=request.POST.get('selectoption')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        global el
        global pro
        el = email
        password=request.POST.get('password')
        gender=request.POST.getlist('gender')
        log=login1(selectoption=selectoption,fname=fname,lname=lname,email=email,password=password,gender=gender)
        pro=profilepatient(fname=fname,lname=lname,email=email,gender=gender)
        emil =  login1.objects.raw("select id,email from service_login1")
        for i in emil:
            if i.email==el:
                j=j+1 
                print(i.email)
        print(j)   
        
        if j!=0 :
            print("hi")
            n="emilid already exist"
            return render(request,"signup.html",{'n':n})
        
        else:    
            otp(el)
            return render(request,"new form.html")
        

def otp(el):
    el=el
    n=''
    global OTP
    OTP = random.randint(11111,99999)
    send_mail(
        'OTP',
        "your login otp is " +str(OTP),
        'vydya.doctor@gmail.com',
        [el],
        #fail_silentv = False,
    )
    
def otpsignp(request):
    if request.method=="POST":
        otp=request.POST.get('otp')
        if otp==str(OTP):
            log.save()
            pro.save()
            
            n="login successful"
            return render(request,"home.html",{'n':n})
        else:
            n='OTP incorrect'
            return render(request,"new form.html",{'n':n})
        
emailid=""      

def forget_email_otp(request):
    global emailid
    n=""
    if request.method=="POST": 
        emailid=request.POST.get('email')
        print(emailid)
        emil =  login1.objects.raw("select * from service_login1 where email = %s",[emailid])
        if len(emil)==0:
            n="no such emailid found"
            return render(request,"froget_emil_otp.html",{'n':n})
        else:
           otp(emailid)
           return render(request,"forget_p_otp.html")

def forget_p_otp(request):
    n=""
    if request.method=="POST":
        otp=request.POST.get('otp')
        pas=request.POST.get('password')
    if otp==str(OTP):
        log=connection.cursor()
        log.execute("UPDATE service_login1 SET password = %s WHERE email= %s",(pas, emailid))
        n="password updated successfully"
        return render(request,"home.html",{'n':n})
    else:
        n="incorrect otp"
        return render(request,"forget_p_otp.html",{'n':n})
        
        
    
        
        
        
        
    
    
        
    
    
        

        
        
def query(request):
    i=0
    a='raghavaganesh9@gmail.com'
    #emil = login1.objects.raw("select id,email from service_login1 where email= %s", [a])
    #emil = login1.objects.raw("select id,email from service_login1 where email='raghavaganesh9@gmail.com' ")
    emil =  login1.objects.raw("select id,email from service_login1")
    # print(emil.id)
    # print(emil.password)
    for i in emil:
       print(i.email)
       
    print(emil[0].email)
    
   
    return render(request,"query.html",{'email':emil[0].email})

            


    