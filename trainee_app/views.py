from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course_app.models import Course
from .forms import  AddTraineeForm

courses = Course.objects.all()

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        form = AddTraineeForm(request.POST)
        if form.is_valid():
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                course=Course.objects.get(id=form.cleaned_data['course'])
            )
            return redirect('trainee_list')
    else:
        form = AddTraineeForm()
    return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})
def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    courses = Course.objects.all()
    context= {'courses': courses,
              'trainee': trainee}
    if request.method == 'POST':
        trainee.name = request.POST['name']
        trainee.age = request.POST['age']
        trainee.email = request.POST['email']
        trainee.course = Course.objects.get(id=request.POST['course'])
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/update_trainee.html', context)

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')
