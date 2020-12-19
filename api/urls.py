from django.urls import path
from api.views import Registrar

urlpatterns = [
    path('registrar/', Registrar.as_view(), name='registro'),
]