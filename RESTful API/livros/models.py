from django.db import models
from uuid import uuid4

def upload_imagens(instance, filename):
    return f"{instance.id_livro}-{filename}"


class Livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()
    estado_livro = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    data_publicacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to=upload_imagens, blank=True, null=True)
