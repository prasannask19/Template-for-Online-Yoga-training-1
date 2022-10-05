from django.shortcuts import render
from django.shortcuts import HttpResponse
from website.models import Signup 
from website.models import contact
# Create your views here.
def home(requests):
    return render(requests, "Home.html")
def crs(requests):
    return HttpResponse("Sorry :( This page will be developed soon")
def con(requests):
     if requests.method=="POST":
        nm=requests.POST['name']
        pno=requests.POST['phno']
        eml=requests.POST['eml']
        desc=requests.POST['desc']
        insp=contact(name=nm,phno=pno,email=eml,text=desc)
        insp.save()
        return HttpResponse("Thank You")
     return render(requests, "Contact.html")
def sgn(requests):
    if requests.method=="POST":
        name=requests.POST['username']
        passwd=requests.POST['Pass']
        dateofb=requests.POST['date']
        phno=requests.POST['Phno']
        print(name,passwd,dateofb,phno)
        ins=Signup(name=name,passwd=passwd,dateofb=dateofb,phno=phno)
        ins.save()
        print("Data saved successfully")
        return render(requests, "Home.html")

    return render(requests, "Signup.html")  
    
def abs(requests):
    return render(requests, "Aboutus.html")

