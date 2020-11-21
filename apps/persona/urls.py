from django.urls import path
from .views import ListaPersonasView

app_name = 'persona'
urlpatterns = [
    # persona views
    path('', ListaPersonasView, name='listapersonas'),

]