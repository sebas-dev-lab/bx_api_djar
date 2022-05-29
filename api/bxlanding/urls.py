from django.urls import path
from .views import getAll, getOne, post

app_name = "bxlanding"


urlpatterns = [
    path('firstSection/', getAll),
    path('firstSection/<int:id>/', getOne),
    path('firstSection/save/', post),
]
