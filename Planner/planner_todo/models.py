from django.db import models


class Note(models.Model):  # https://www.youtube.com/watch?v=4EJlrweJE-M
    title = models.CharField(max_length=100)
    begin_date = models.DateField(auto_created=True)
    end_date = models.DateField()
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    finished = models.BooleanField()

    def __str__(self):
        return self.title


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    updated = models.DateField(auto_now=True)
    finished = models.BooleanField()

    class Meta:
        ordering = ('finished',)

    def __str__(self):
        return self.title
