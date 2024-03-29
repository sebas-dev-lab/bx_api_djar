from django.urls import path
from .views import BlogListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path('posts/', BlogListView.as_view()),
    path('posts/save/', BlogListView.as_view()),
    path('posts/<post_slug>/', PostDetailView.as_view()),
    path('update/<post_slug>/', PostDetailView.as_view()),
    path('delete/<post_slug>/', PostDetailView.as_view()),
]
