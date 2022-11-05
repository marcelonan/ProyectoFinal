from django.urls import path
from .views import inicio, nosotros, productos, tienda, reseña
from AppFinal import views


urlpatterns = [
    path('inicio/',inicio),
    path('nosotros/',nosotros),
    path('productos/',productos),
    path('tienda/',tienda),
    path('reseña/',reseña)
]