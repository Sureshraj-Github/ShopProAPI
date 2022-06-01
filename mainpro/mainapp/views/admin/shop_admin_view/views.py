from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from . import serializers as admin_view_serializer
from mainpro import utils as project_utils
from mainapp.models.admin.shop_admin_view import ShopAdminView as shop_admin_view_model


@api_view(["GET"])
def shop_admin_view(request):
    serializer = admin_view_serializer.ShopAdminView(data=request.data)
    serializer.is_valid(raise_exception=True)
    # serializer.save()
    shop_admin_views = shop_admin_view_model.objects.all()
    serializer = admin_view_serializer.ShopAdminView(shop_admin_views, many=True)
    return Response(project_utils.success_response(data=serializer.data, msg="Data Fetched Successfully",
                                                   status_code=status.HTTP_200_OK))
