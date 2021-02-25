from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views
from users.views import register
import django.contrib.auth.urls as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('', views.IndexArticle.as_view(), name='index'),
    path('register/', register, name='register'),
    path('', include(accounts)),

    # REST API
    path('shop-api/', include('API.urls', 'api_'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
