from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import NhanVienVanPhong, NhanVienSanXuat, NhanVienQuanLy, BangNhanVien


def render_index(request):
    return render(request, "index.html")


def get_danh_sach_nhan_vien_chua_tinh_luong(request):
    if request.method == "GET":
        try:
            nhan_vien_classes = [NhanVienVanPhong, NhanVienSanXuat, NhanVienQuanLy]
            for nhan_vien_class in nhan_vien_classes:
                for nv in nhan_vien_class.objects.all():
                    nv.luong_hang_thang = 0
                    nv.save()
            data = BangNhanVien.objects.all().values()
            return JsonResponse(list(data), safe=False)
        except Exception as e:
            error_message = str(e)
            return HttpResponse("Error: {}".format(error_message), status=500)


def get_danh_sach_nhan_vien_tinh_luong(request):
    if request.method == "GET":
        try:
            nhan_vien_classes = [NhanVienVanPhong, NhanVienSanXuat, NhanVienQuanLy]
            for nhan_vien_class in nhan_vien_classes:
                for nv in nhan_vien_class.objects.all():
                    nv.luong_hang_thang = nv.tinh_luong()
                    nv.save()
            data = BangNhanVien.objects.all().values()
            return JsonResponse(list(data), safe=False)
        except Exception as e:
            error_message = str(e)
            return HttpResponse("Error: {}".format(error_message), status=500)


def get_nhan_vien_by_manv(request, manv):
    if request.method == "GET":
        try:
            data = BangNhanVien.objects.all().values().filter(ma_nv=manv)
            return JsonResponse(list(data), safe=False)
        except Exception as e:
            error_message = str(e)
            return HttpResponse("Error: {}".format(error_message), status=500)
