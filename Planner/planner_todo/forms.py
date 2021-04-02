from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'finished',)

    # def __init__(self, *args, **kwargs):
    #     super(ToDoForm, self).__init__(*args, **kwargs)
