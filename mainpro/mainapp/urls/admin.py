from django.urls import path
from mainapp.views.admin.shop_admin_view import views as shop_admin_view_views

urlpatterns = [
    path("shop_admin_view", shop_admin_view_views.shop_admin_view,
         name='admin-shop-admin-view'),
]
