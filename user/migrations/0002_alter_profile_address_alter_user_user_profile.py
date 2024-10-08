# Generated by Django 5.0.7 on 2024-08-11 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
