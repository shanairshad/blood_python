# Generated by Django 4.0.4 on 2022-07-28 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_auto_20210810_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='city',
            new_name='center',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='state',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='requestblood',
            old_name='city',
            new_name='center',
        ),
        migrations.RenameField(
            model_name='requestblood',
            old_name='state',
            new_name='district',
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('center', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField(default='', max_length=500)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bloodgroup')),
                ('donor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
