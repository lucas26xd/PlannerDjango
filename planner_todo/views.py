from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from calendar import monthcalendar, setfirstweekday, SUNDAY
from datetime import datetime
from .models import Note, ToDo
from .forms import ToDoForm

MONTH_NAMES = ('', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', )
month_number = year = 0


def planner_list(request):
    global month_number, year
    if request.method == 'POST':
        # print('-' * 30, request.POST)
        if 'previous' in request.POST:  # Calendário
            month_number = int(request.POST['previous']) - 1
            year = int(request.POST['year'])
            month_number = 12 if month_number == 0 else month_number
            year = year - 1 if month_number == 12 else year
        elif 'next' in request.POST:
            month_number = int(request.POST['next']) + 1
            year = int(request.POST['year'])
            month_number = 1 if month_number == 13 else month_number
            year = year + 1 if month_number == 1 else year
        else:  # ToDo
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

    if month_number == 0 or year == 0:  # Primeiro início
        now = datetime.now()
        month_number = now.month
        year = now.year
    month = MONTH_NAMES[month_number]
    setfirstweekday(SUNDAY)
    calendario = monthcalendar(year, month_number)

    context = {'month': month,
               'month_number': month_number,
               'year': year,
               'calendario': calendario,
               'Notes': Note.objects.all(),
               'ToDo': ToDo.objects.all()}
    return render(request, 'planner_todo/planner_list.html', context)

