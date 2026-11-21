from django.shortcuts import render,redirect,get_object_or_404
from core.forms import RegisterForm,StudentForm
from core.models import Students
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

#Registration Part
def register_view(request):
    if request.user.is_authenticated:
        return redirect ("view_All_Student")
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration Successful.")
            return redirect('view_All_Student')
        # Bug fix #1: pass the form (with errors) back so the template can render them
        return render(request,"register.html",{"form":form,"message":"Invalid Registration. Please try again"})
    else:
        form = RegisterForm()
    return render(request,"register.html",{"form":form})

#Login Part
def login_view(request):
    if request.user.is_authenticated:
        return redirect('view_All_Student')
    error = None
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username = username, password = password)
       if user is not None:
           login(request,user)
           return redirect('view_All_Student')
       return render(request,'login.html',{"message":"Invalid username or password."})
    return render(request,'login.html',{"error":error})

#Add student 
@login_required
def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('view_All_Student')
        # Bug fix #2: pass the form (with errors) back so the template can render them
        return render(request,'addStudent.html',{'form':form,'message':'Invalid Input. Please try again'})
    else:
        form = StudentForm()
    return render(request,'addStudent.html',{"form":form})
    
#Search Student by id 
@login_required
def searchStudent(request):
    if request.method == 'POST':
        sid = request.POST.get("sid","").strip()
        student = Students.objects.filter(sid = sid).first()
        if student:
            return render(request,'searchStudent.html',{"student":student})
        # Bug fix #3: typo "Studetn" → "Student"
        return render(request,'searchStudent.html',{"message":"No Student found"})
    return render(request,"searchStudent.html")

#view All Student
@login_required
def view_All_Student(request):
    student = Students.objects.all().order_by("sid")
    return render(request,'view_All_Student.html',{"student":student})

#Update Student step1: Serach student by id first
@login_required
def updateStudent(request):
    if request.method == 'POST':
        sid = request.POST.get("sid","").strip()
        student = Students.objects.filter(sid = sid).first()
        if student:
            return redirect("editStudent",pk=student.pk)
        return render(request,"updateStudent.html",{"message":"No Student found"})
    return render(request,'updateStudent.html')

#Update Student step2: edit data
@login_required
def editStudent(request,pk):
    student = get_object_or_404(Students,pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance = student)
        if form.is_valid():
            form.save()
            return redirect("view_All_Student")
        # Bug fix #4: pass the form (with errors) AND student back so the template can re-render
        return render(request,"editStudent.html",{"form":form,"student":student,"message":"Invalid Input. Try again"})
    else:
        form = StudentForm(instance = student)
    return render(request,"editStudent.html",{"form":form, "student":student})

#Delete Student 
@login_required
def deleteStudent(request):
    if request.method == 'POST':
        sid = request.POST.get("sid","").strip()
        student = Students.objects.filter(sid = sid).first()
        if student:
            if student.image:
                student.image.delete(save = False) #remove the file from disk too
            student.delete()
            return redirect('view_All_Student')
        return render(request,"deleteStudent.html",{"message":"No student found"})
    return render(request,"deleteStudent.html")
        
#log out part
# Bug fix #5: remove dead unreachable code — @require_POST already enforces POST-only,
# so the inner `if request.method == 'POST':` check and the else branch were never reachable.
@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


