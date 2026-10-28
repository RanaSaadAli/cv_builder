from django.shortcuts import render, redirect
from .models import Skill
from .forms import SkillForm

# Create your views here.
def skill_list(request):
    skill = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {'skills':skill})

def add_skill(request):
    if request.method =='POST':
        #handle form submision
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        #show an empty form
        form = SkillForm()

    return render(request, 'skills/add_skill.html', {'form':form})


def edit_skill(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')

    else:
        form = SkillForm(instance=skill)
    return render(request, 'skills/edit_skill.html', {'form':form})

def delete_skill(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    skill.delete()
    return redirect('skill_list')
    