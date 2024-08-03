from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),   
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history' , views.order_history , name = "order_history")
]
