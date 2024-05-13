from django.urls import path
from . import views

urlpatterns = [
    path("bangnhanvien/tinhluong/<int:manv>/", views.get_nhan_vien_by_manv, name="nhanvienbyid"),
    path("bangnhanvien/tinhluong", views.get_danh_sach_nhan_vien_tinh_luong, name='bangnhanvientinhluong'),
    path("bangnhanvien/", views.get_danh_sach_nhan_vien_chua_tinh_luong, name="bangnhanvien"),
    path("", views.render_index, name="render"),
]
