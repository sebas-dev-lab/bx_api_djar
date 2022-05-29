from django.urls import path
from .views import *

app_name = "bxlanding"


urlpatterns = [
    path('fsSection/', getAll),
    path('fsSection/<int:id>/', getOne),
    path('fsSection/save/', post),
    path('abSection/', getAboutSectionAll),
    path('abSection/<int:id>/', getAboutSection),
    path('abSection/save/', createNewAboutSection),
    path('shSection/', getAllShowSection),
    path('shSection/<int:id>/', getOneShowSectionById),
    path('shSection/save/', createShowSection),
    path('prSection/', getAllPresentation),
    path('prSection/<int:id>/', getOnePresentation),
    path('prSection/save/', createNewPresentation),
]
