from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        Trainee.objects.create(name=name, age=age, email=email)
        return redirect('trainee_list')
    return render(request, 'trainee/add_trainee.html')

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.name = request.POST['name']
        trainee.age = request.POST['age']
        trainee.email = request.POST['email']
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')
