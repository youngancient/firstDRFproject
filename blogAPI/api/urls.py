from django.urls import path, include
from .views import ListBlogView, CreateBlogView

urlpatterns = [
    path('list/', ListBlogView.as_view(), name='list'),
    path('create/', CreateBlogView.as_view(), name='create'),
]
