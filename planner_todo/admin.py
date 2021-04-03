from django.contrib import admin
from .models import Note, ToDo


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'finished', 'updated']
    list_editable = ['title', 'finished',]
