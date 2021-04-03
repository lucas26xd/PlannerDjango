from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from calendar import HTMLCalendar, month_name
from datetime import datetime
from .models import Note, ToDo
from .forms import ToDoForm

MONTH_NAMES = ('', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', )


def planner_list(request):
    if request.method == 'POST':
        print('-' * 30, request.POST)
        if 'delete' in request.POST:
            todo = ToDo.objects.get(pk=request.POST['id'])
            todo.delete()
        else:
            if 'id' in request.POST:
                todo = ToDo.objects.get(pk=request.POST['id'])
                form = ToDoForm(request.POST, instance=todo)
            else:
                form = ToDoForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print('NÃO VÁLIDO')
        messages.success(request, 'Success!')
        return HttpResponseRedirect(request.path)

    now = datetime.now()
    month = MONTH_NAMES[now.month]
    month_number = now.month
    year = now.year
    calendario = HTMLCalendar().formatmonth(year, month_number)

    context = {'month': month,
               'year': year,
               'calendario': calendario,
               'Notes': Note.objects.all(),
               'ToDo': ToDo.objects.all()}
    return render(request, 'planner_todo/planner_list.html', context)

