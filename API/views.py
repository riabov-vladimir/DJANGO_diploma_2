from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import *
from API.serializers import CategorySerializer


@api_view(['GET'])
def api_detail_category_view(request, id):

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def api_all_category_view(request):

    try:
        category = Category.objects.all()
    except Category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)
