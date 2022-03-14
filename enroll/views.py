from django.shortcuts import render,HttpResponseRedirect
# importing StudentRegistration class from enroll/forms.py
from enroll.forms import StudentRegistration
from .models import User
# Create your views here.
# This function will ad new item and show all iteams
def addshowPage(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email = em, password = pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud})
#this function will edit or update
def updateUser(request,id):
    # if method of the form is POST then this will execute to update a form
    if request.method == 'POST':
        # for updating the value in data base
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance = pi)
        # if all the data is valid then it will save to database
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance = pi) 
    return render(request,'enroll/updatestudent.html',{'form':fm})

# this function will delete item
def deleteUser(request,id):
    # when delete button is press then
    # post method is triggered and 
    # it will store all the object data in pi and delete it
    # Page is reload
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')