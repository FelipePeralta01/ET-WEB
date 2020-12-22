from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mainstore', views.mainstore, name="mainstore"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),
    path('profileadmin/', views.profileadmin, name="profileadmin"),
    path('register/', views.register, name="register"),
]