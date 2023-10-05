from . import views
from django.urls import path
app_name='shopp'
urlpatterns = [

    path('',views.allproductCat,name='allproductCat'),

    path('<slug:c_slug>/',views.allproductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='ProdCatDetail'),


]