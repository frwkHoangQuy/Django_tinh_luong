# Generated by Django 4.1 on 2024-05-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NhanVienQuanLy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nv', models.IntegerField()),
                ('ho_ten', models.CharField(max_length=50)),
                ('luong_co_ban', models.IntegerField()),
                ('luong_hang_thang', models.IntegerField(default=None)),
                ('he_so_chuc_vu', models.DecimalField(decimal_places=1, max_digits=2)),
                ('thuong', models.IntegerField()),
            ],
            options={
                'db_table': 'nhan_vien_quan_ly',
            },
        ),
        migrations.CreateModel(
            name='NhanVienSanXuat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nv', models.IntegerField()),
                ('ho_ten', models.CharField(max_length=50)),
                ('luong_co_ban', models.IntegerField()),
                ('luong_hang_thang', models.IntegerField(default=None)),
                ('so_san_pham', models.IntegerField()),
            ],
            options={
                'db_table': 'nhan_vien_san_xuat',
            },
        ),
        migrations.CreateModel(
            name='NhanVienVanPhong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nv', models.IntegerField()),
                ('ho_ten', models.CharField(max_length=50)),
                ('luong_co_ban', models.IntegerField()),
                ('luong_hang_thang', models.IntegerField(default=None)),
                ('so_gio_lam', models.IntegerField()),
            ],
            options={
                'db_table': 'nhan_vien_van_phong',
            },
        ),
    ]
