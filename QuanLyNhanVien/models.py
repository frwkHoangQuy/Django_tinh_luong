from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class NhanVien(models.Model):
    class Meta:
        abstract = True

    ma_nv = models.IntegerField()
    ho_ten = models.CharField(max_length=50)
    luong_co_ban = models.IntegerField()
    luong_hang_thang = models.IntegerField(default=0)

    def tinh_luong(self):
        pass


class NhanVienVanPhong(NhanVien):
    class Meta:
        db_table = "nhan_vien_van_phong"

    so_gio_lam = models.IntegerField()

    def tinh_luong(self):
        return 100 + (
            self.luong_co_ban
            + self.so_gio_lam * 220000
            + (5000000 if self.so_gio_lam > 100 else 0)
        )


class NhanVienSanXuat(NhanVien):
    class Meta:
        db_table = "nhan_vien_san_xuat"

    so_san_pham = models.IntegerField()

    def tinh_luong(self):
        luong = self.luong_co_ban + self.so_san_pham * 175000
        luong = luong * 1.2 if self.so_san_pham > 150 else luong
        return luong


class NhanVienQuanLy(NhanVien):
    class Meta:
        db_table = "nhan_vien_quan_ly"

    he_so_chuc_vu = models.DecimalField(max_digits=2, decimal_places=1)
    thuong = models.IntegerField()

    def tinh_luong(self):
        return self.luong_co_ban * self.he_so_chuc_vu + self.thuong


class BangNhanVien(models.Model):
    ma_nv = models.IntegerField(default=0)
    ho_ten = models.CharField(max_length=50, default="")
    luong_hang_thang = models.IntegerField(default=0)


@receiver(post_save, sender=NhanVienVanPhong)
@receiver(post_save, sender=NhanVienSanXuat)
@receiver(post_save, sender=NhanVienQuanLy)
def update_bang_nhan_vien(sender, instance, created, **kwargs):
    BangNhanVien.objects.update_or_create(
        ma_nv=instance.ma_nv,
        defaults={
            "ho_ten": instance.ho_ten,
            "luong_hang_thang": instance.luong_hang_thang,
        },
    )


@receiver(post_delete, sender=NhanVienVanPhong)
@receiver(post_delete, sender=NhanVienSanXuat)
@receiver(post_delete, sender=NhanVienQuanLy)
def delete_bang_nhan_vien(sender, instance, **kwargs):
    BangNhanVien.objects.filter(ma_nv=instance.ma_nv).delete()
