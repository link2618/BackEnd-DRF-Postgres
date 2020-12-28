from django.urls import path
from api.views import Registrar, Login, Logout

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('registrar/', Registrar.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
    #path('logout/<uuid:id>', Logout.as_view(), name='logout'),
    path('logout/', Logout.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='obtener_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]