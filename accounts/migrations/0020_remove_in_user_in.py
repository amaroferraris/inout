# Generated by Django 4.1.1 on 2023-08-17 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_in_user_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='in',
            name='user_in',
        ),
    ]