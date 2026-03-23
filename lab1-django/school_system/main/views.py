

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student, Feedback


def home(request):
    return render(request, 'home.html')


def students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            image=image
        )

        return redirect('students')

    all_students = Student.objects.all()
    return render(request, 'students.html', {'students': all_students})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(
            email=email,
            message=message
        )

        return redirect('contact')

    return render(request, 'contact.html')