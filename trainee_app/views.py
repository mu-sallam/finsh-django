from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course_app.models import Course
from .forms import  AddTraineeForm
from django.views import View


courses = Course.objects.all()

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

class AddTraineeView(View):
    template_name = 'trainee/add_trainee.html'
    
    def get(self, request):
        form = AddTraineeForm()
        return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})
    
    def post(self, request):
        form = AddTraineeForm(request.POST)
        if form.is_valid():
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                course=Course.objects.get(id=form.cleaned_data['course'])
            )
            return redirect('trainee_list')
        return render(request, 'trainee/add_trainee.html', {'form': form, 'courses': courses})

class UpdateTraineeView(View):
    template_name = 'trainee/update_trainee.html'
    
    def get(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        courses = Course.objects.all()
        context = {'courses': courses, 'trainee': trainee}
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        trainee.name = request.POST['name']
        trainee.age = request.POST['age']
        trainee.email = request.POST['email']
        trainee.course = Course.objects.get(id=request.POST['course'])
        trainee.save()
        return redirect('trainee_list')

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')
