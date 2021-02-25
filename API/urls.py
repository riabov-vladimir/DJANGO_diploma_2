from django.urls import path
from API.views import *

app_name = 'API'

urlpatterns = [
    path('<id>/', api_detail_category_view, name='category_detail'),
    path('', api_all_category_view, name='category_detail'),
    path('delete/<id>/', api_delete_category_view, name='category_delete'),
]
