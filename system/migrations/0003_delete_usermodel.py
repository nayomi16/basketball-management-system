# Generated by Django 3.2.7 on 2021-10-08 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_rolemodel_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
