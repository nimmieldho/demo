from . import views
from django.urls import path

app_name = 'cart'
urlpatterns = [

    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_Detail, name='cart_Detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
    path('payment/',views.payment,name='payment'),
]
