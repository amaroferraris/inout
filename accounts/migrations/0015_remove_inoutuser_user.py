# Generated by Django 4.1.1 on 2022-12-31 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_inoutuser_alter_in_user_in_alter_out_user_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inoutuser',
            name='user',
        ),
    ]
