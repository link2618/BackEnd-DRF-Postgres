from django.urls import path
from api.views import Registrar, Login

urlpatterns = [
    path('registrar/', Registrar.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
]