# Generated by Django 4.1.1 on 2022-12-30 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in',
            name='user_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
