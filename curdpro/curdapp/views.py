from django.shortcuts import render, redirect
from .models import empdata

def homepage(request):
    emp1=empdata.objects.all()
    return render(request,'addingmain.html', {'emp':emp1})



def addingmain(request):
    if request.method == 'GET':
        return render(request,'homepage.html')
    else:
        empdata(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        company=request.POST['company'],
        salary=request.POST['salary'],
        location=request.POST['location'],
        ).save()
        return redirect(homepage)




def updata(request,id):
    emp=empdata.objects.get(id=id)
    return render(request,'updating.html',{'i':emp})



def updating_emp(request,id):
    emp=empdata.objects.get(id=id)
    emp.first_name=request.POST['fname']
    emp.last_name=request.POST['lname']
    emp.email=request.POST['email']
    emp.mobile=request.POST['mobile']
    emp.company=request.POST['company']
    emp.salary=request.POST['salary']
    emp.location=request.POST['location']
    emp.save()
    return redirect(homepage)





def delete_emp(request,id):
    emp=empdata.objects.get(id=id)
    emp.delete()
    return redirect(homepage)
