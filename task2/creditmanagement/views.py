from django.shortcuts import render,redirect
from .models import AddUser
from .models import TransferMoney
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'creditmanagement/home.html')
def aboutus(request):
    return render(request,'creditmanagement/about.html')
def viewuser(request):
    users=None
    users = AddUser.objects.all()
    if users!=None:
        return render(request,'creditmanagement/viewuser.html',{'users':users})
    else:    
        return render(request,'creditmanagement/viewuser.html')
def adduser(request):
    flag=False
    if request.method=='GET':
        return render(request,'creditmanagement/adduser.html')
    if request.method=='POST':

        Name=request.POST['Name']
        email=request.POST['email']
        credit=request.POST['credit']
        
        if Name!='' and email!='' and credit!='':
            credit=int(credit)
            na=AddUser.objects.filter(Name=Name)
            if na:
                flag=True
                messages.warning(request, 'The User Name already exists.')
                return render(request,'creditmanagement/adduser.html',{'f':flag})
            else:
                if credit>=0 and credit<=50:
                    flag='True'
                    u=AddUser.objects.create(Name=Name,email=email,credit=credit)
                    messages.warning(request, 'The User Added Sucessfully.')
                    return render(request,'creditmanagement/adduser.html',{'f':flag})
                else:
                    flag=True
                    messages.warning(request, 'Please Enter credits within the range.')
                    return render(request,'creditmanagement/adduser.html',{'f':flag})
        else:
            flag=True
            messages.warning(request, 'Please Enter All the details.')
        return render(request,'creditmanagement/adduser.html',{'f':flag})

def transfer(request):
    a,b=None,None
    flag1=False
    transfers=TransferMoney.objects.all()
    if request.method=='GET':
        

        if transfers!=None:
            return render(request,'creditmanagement/transfer.html',{'trans':transfers}) 
        else:
            return render(request,'creditmanagement/transfer.html')
    if request.method=='POST':
        a1,b1=None,None
        sid=request.POST['sid']
        rid=request.POST['rid']
        money=request.POST['money']
        if sid!='' and rid!='' and money!='':
            money=int(money)
            if money>=0 and money<=50:
                a1=AddUser.objects.filter(id=sid)
                b1=AddUser.objects.filter(id=rid)
                if a1 and b1:
                    a=AddUser.objects.get(id=sid) #sender
                    #if money>=a.credit and money>=0:
                    sname=a.Name
                    b=AddUser.objects.get(id=rid) #reaciver
                    acredit= a.credit-money
                    if acredit>=0:
                        a.credit=acredit
                        a.save()
                        bcredit=b.credit+money
                        b.credit=bcredit
                        b.save()  
                        rname=b.Name
                        v=TransferMoney.objects.create(SenderName=sname,ReName=rname,Credits=money)
                        flag1=True
                        messages.warning(request, 'Transaction Done Sucessfully.')
                        return render(request,'creditmanagement/transfer.html',{'f':flag1,'trans':transfers})
                    else:
                        flag1=True
                        messages.warning(request, 'The Sender does\'nt have the sufficient balance.')
                        return render(request,'creditmanagement/transfer.html',{'f':flag1,'trans':transfers})
                else:
                    flag1=True
                    messages.warning(request, 'Please Enter Valid User ID\'s.')
                    return render(request,'creditmanagement/transfer.html',{'f':flag1,'trans':transfers})
            else:
                flag1=True
                messages.warning(request, 'Please Enter Limited share within the range.')
                return render(request,'creditmanagement/transfer.html',{'f':flag1,'trans':transfers})
        else:
            flag1=True
            messages.warning(request, 'Please Enter All the details.')
            return render(request,'creditmanagement/transfer.html',{'f':flag1,'trans':transfers})
