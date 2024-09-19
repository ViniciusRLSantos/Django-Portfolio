from django.urls import path
from . import views
#from .views import PostView, index, post_view

urlpatterns = [
    path('home/', views.index),
    path('create/', views.create_post),
    path('post/<int:id>/', views.post_view),
    path('update/<int:id>/', views.update_view),
]