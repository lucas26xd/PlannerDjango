from django.shortcuts import render
from .models import Note, ToDo
from .forms import ToDoForm


def planner_list(request):
    if request.method == 'POST':
        print('-' * 30, request.POST)
        if 'id' in request.POST:
            todo = ToDo.objects.get(pk=request.POST['id'])
            form = ToDoForm(request.POST, instance=todo)
        else:
            form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('NÃO VÁLIDO')
    context = {'month_year': 'Abril de 2021',
               'Notes': Note.objects.all(),
               'ToDo': ToDo.objects.all()}
    return render(request, 'planner_todo/planner_list.html', context)
