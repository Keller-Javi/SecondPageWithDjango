from django.db import models
# un modelo de usuario creado por django
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Se añade la fecha y la hora al crear una instancia
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    # Hacemos una relación entre la tarea creada y el usuario que la creó
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # y el on_delete=models.CASCADE quiere decir que si se elimina el usuario se van a eliminar las tareas relacionadas con el

    def __str__(self):
        return self.title
