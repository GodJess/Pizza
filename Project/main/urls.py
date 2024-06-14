from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/about', views.about, name="about"),
    path('/paneladmin', views.paneladmin, name="paneladmin" ),
    path('/all', views.all, name="all"),
    path('/combo', views.combo, name="combo"),
    path('/drink', views.drink, name="drink"),
    path('/dessert', views.dessert, name="dessert"),
    path('/role', views.role, name="role"),
    path('<int:pk>', views.NewDatailViewProduct.as_view(), name="product-detail"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]