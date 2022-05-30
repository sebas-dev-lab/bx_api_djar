from django.urls import path
from .views import *

app_name = "authorization"


urlpatterns = [
    path('', getAllUsers),
    path('<int:id>/', getOneUserById),
    path('save/', createNewUser),
]
