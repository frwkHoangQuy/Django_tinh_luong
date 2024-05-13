from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('QuanLyNhanVien.urls')),
    path('admin/', admin.site.urls),
]
