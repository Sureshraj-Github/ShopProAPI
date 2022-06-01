from rest_framework import serializers
from mainapp.models.admin import shop_admin_view as shop_admin_view_model


class ShopAdminView(serializers.ModelSerializer):
    class Meta:
        model = shop_admin_view_model.ShopAdminView
        fields = "__all__"
