from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from .forms import StudentForm


def students_list(request):
    students = Students.objects.all().order_by("student_id")
    return render(request, "student/students_list.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm()

    return render(request, "student/add_student.html", {"form": form})


def edit_student(request, id):
    student = get_object_or_404(Students, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "student/add_student.html", {"form": form})


def delete_student(request, id):
    student = get_object_or_404(Students, id=id)
    student.delete()
    return redirect("students_list")
