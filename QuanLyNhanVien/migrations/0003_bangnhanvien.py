# Generated by Django 4.1 on 2024-05-13 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyNhanVien', '0002_alter_nhanvienquanly_luong_hang_thang_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BangNhanVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nhan_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuanLyNhanVien.nhanviensanxuat')),
            ],
        ),
    ]