from django.urls import path
from .views import FirsSectionView

app_name = "bxlanding"

urlpatterns = [
    path('firstSection/', FirsSectionView.as_view()),
    path('firstSection/save/', FirsSectionView.as_view()),
]
