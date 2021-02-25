from django.urls import path
from API.views import api_detail_category_view

app_name = 'API'

urlpatterns = [
    path('<slug>/', api_detail_category_view, name='category_detail')
]
