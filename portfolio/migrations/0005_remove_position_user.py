# Generated by Django 2.2.1 on 2019-06-20 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190619_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='user',
        ),
    ]
