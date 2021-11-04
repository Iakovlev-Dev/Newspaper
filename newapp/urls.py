from django.urls import path
from django.contrib import admin
from django.urls import include
from .views import PostDetail, PostList, Search, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('create/', PostCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]