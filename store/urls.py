from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mainstore', views.mainstore.as_view(), name="mainstore"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('login/', views.login, name="login"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('logout/', views.logout, name="logout"),
    path('admin_products/', views.admin_products.as_view(), name="admin_products"),
    path('delete_product/<id>', views.delete_product, name="delete_product"),
    path('update_product/<id>', views.update_product, name="update_product"),
]