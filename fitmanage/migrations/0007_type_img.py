# Generated by Django 4.2.5 on 2023-09-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitmanage', '0006_alter_addmember_address_alter_trainer_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='img',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
