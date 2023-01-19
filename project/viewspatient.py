from django.http import HttpResponse
from django.shortcuts import render
from service.models import login1
from django.core.mail import send_mail
from django.db import connection
from service.models import profilepatient

emailid=""
fname=""
lname=""
bloodgroup=""
gender=""
phone=""
dateofbirth=""
address=""

def gain(emil,fn,ln,g):
    global emailid
    emailid=emil
    global fname
    fname=fn
    global lname
    lname=ln
    global gender
    gender=g
    
def pedit(request):
    global emailid
    global fname
    global lname
    global bloodgroup
    global gender
    global phone 
    global dateofbirth
    global address
    m=""
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        bloodgroup=request.POST.get('bloodgroup')
        emailid=request.POST.get('email')
        gender=request.POST.get('Gender')
        phone=request.POST.get('phone')
        dateofbirth=request.POST.get('dateofbirth')
        address=request.POST.get('address')
        print(address)
        
        cursor=connection.cursor()
        cursor.execute("update service_profilepatient set fname=%s,lname=%s,bloodgroup=%s,email=%s,gender=%s,phone=%s,dateofbirth=%s,address=%s where email = %s ",[fname,lname,bloodgroup,emailid,gender,phone,dateofbirth,address,emailid])
        m="edit is success"
        
    return render(request,"indexpatient.html",{'m':m})
        
        
     
def indexpatient(request):
    n=""
    return render(request,"indexpatient.html")

def about(request):
    return render(request,"pabout.html")

def service(request):
    return render(request,"pservice.html")

def doctors(request):
    return render(request,"pteam.html")

def appointment(request):
    return render(request,"pappointment.html")

def search(request):
    return render(request,"psearch.html")

def contact(request):
    return render(request,"pcontact.html")

def editprofile(request):
    global emailid
    a=profilepatient.objects.raw("select * from service_profilepatient where email = %s ",[emailid])
    
    return render(request,"pedit.html",{'a':a[0]})

def logout(request):
    return render(request,"home.html")



def emergencycare(request):
     return render(request,"indexpatient.html")
 
def operationandsurgery(request):
     return render(request,"indexpatient.html")
 
def ctscan(request):
     return render(request,"indexpatient.html")
 
def othertest(request):
     return render(request,"indexpatient.html")

def medicineandpharmacy(request):
     return render(request,"indexpatient.html")

def bloodtest(request):
     return render(request,"indexpatient.html")
 
def helpandsupport(request):
    return render(request,"indexpatient.html")






