from django.urls import path

from .views import PostList, PostDetail, add_post, edit_post, delete_post

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('post/new/', add_post, name='add_post'),
    path('post/<int:pk>/edit/', edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
]