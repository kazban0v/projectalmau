from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def home(request):
    university_info = "Алматы Менеджмент Университет"
    return render(request, 'university/home.html', {'university_info': university_info})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'university/register_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'university/student_list.html', {'students': students})


def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'university/student_detail.html', {'student': student})


def delete(request, id):
    try:
        user = Student.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/students/")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>User does not exit<\h2>") 

