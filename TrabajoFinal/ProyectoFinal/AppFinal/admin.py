from django.contrib import admin

from .models import productos, reseñas, tienda

# Register your models here.
admin.site.register(productos)
admin.site.register(reseñas)
admin.site.register(tienda)

