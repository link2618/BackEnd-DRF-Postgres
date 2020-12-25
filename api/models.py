from django.db import models

import uuid
import datetime
import hashlib

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, help_text='Nombre del usuario')
    lastName = models.CharField(max_length=100, help_text='Apellido del usuario')
    date = models.DateField()
    # Automatica mente se pone la fecha cuando se crea con la propiedad 'auto_now_add'
    dateCreated = models.DateTimeField('Fecha De Creación', auto_now_add=True)
    # esta fecha se modifica cada vez que se realice una accion 'auto_now'
    dateUpdated = models.DateTimeField('Fecha de Modificacion', auto_now=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, help_text='Contraseña del usuario')
    tipo = models.CharField(max_length=100, help_text='Tipo de Usuario', default='CLIENTE', blank=True)

    '''
    def __init__(self, name, lastName, date, email, password, tipo):
        super(User, self).__init__()
        self.id = str(uuid.uuid4())
        self.name = name
        self.lastName = lastName
        self.date = date
        self.email = email
        self.password = password
        self.tipo = tipo

    def __init__(self, email, password):
        super(User, self).__init__()
        self.email = email
        self.password = password
    '''

    def __str__(self):
        return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.tipo = self.tipo.upper()
        hoy = datetime.date.today()
        if (hoy.month > self.date.month):
            self.age = hoy.year - self.date.year
        else:
            self.age = (hoy.year - self.date.year) - 1
        if self.tipo == '':
            self.tipo = 'CLIENTE'
        #Encriptar contraseña
        password = hashlib.sha256(str(self.password).encode('utf-8'))
        self.password = password.hexdigest()
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Users"