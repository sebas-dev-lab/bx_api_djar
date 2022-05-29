from django.urls import path
from .views import *

app_name = "bxlanding"


urlpatterns = [
    path('firstSection/', getAll),
    path('firstSection/<int:id>/', getOne),
    path('firstSection/save/', post),
    path('abSection/', getAboutSectionAll),
    path('abSection/<int:id>/', getAboutSection),
    path('abSection/save/', createNewAboutSection),

]
