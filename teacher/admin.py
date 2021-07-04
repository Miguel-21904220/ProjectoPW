from django.contrib import admin

# Register your models here.
from .models import Formulario, Quiz, Comment 

admin.site.register(Formulario)
admin.site.register(Quiz)
admin.site.register(Comment)