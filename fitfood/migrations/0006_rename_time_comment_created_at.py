# Generated by Django 4.2.5 on 2023-09-14 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitfood', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='time',
            new_name='created_at',
        ),
    ]