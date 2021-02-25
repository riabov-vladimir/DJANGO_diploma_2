from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import *
from API.serializers import CategorySerializer


@api_view(['GET'])
def api_detail_category_view(request, slug):

    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)