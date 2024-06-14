from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name="account"),
    path('snake', views.snake, name="snake"),
    path('tetris', views.tetris, name="tetris"),
    path('avtoriz', views.avtoriz, name="avtoriz"),
    path('register', views.register, name="register"),
    path('personal_data', views.personal_data, name='persdata'),
    path('add_name/', views.add_name, name="add_name")
]