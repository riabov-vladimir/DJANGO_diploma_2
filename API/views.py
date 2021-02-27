from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import *
from API.serializers import CategorySerializer


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail_category_view(request, id):
    print('api_detail_category_view')
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=f'Запись номер {id} успешно обновлена')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        object_deletion = category.delete()
        if object_deletion:
            return Response(status=status.HTTP_200_OK, data=f'Запись номер {id} успешно удалена')
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_all_category_view(request):
    print('api_all_category_view')
    try:
        category = Category.objects.all()
    except Category.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


# @api_view(['PUT'])
# def api_detail_category_view(request, id):
#     print('api_detail_category_view')
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExists:
#         return Response(status=status.HTTP_404_NOT_FOUND)



#
# @api_view(['DELETE'])
# def api_delete_category_view(request, id):
#     print('api_delete_category_view')
#     try:
#         category = Category.objects.de(id=id)
#     except Category.DoesNotExists:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     object_deletion = category.delete()
#     if object_deletion:
#         return Response(status=status.HTTP_200_OK, data=f'Запись номер {id} успешно удалена')
#
#     return Response(status=status.HTTP_400_BAD_REQUEST)
