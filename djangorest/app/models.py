from django.db import models

class Todo(models.Model):
    nome = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
