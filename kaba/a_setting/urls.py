from django.contrib import admin
from django.urls import path, include
# для подключения картинок
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Пользователи
    path('users/', include('allauth.urls')),
    # сервис реклама 
    path('ad/', include('ad.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)