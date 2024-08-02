# Generated by Django 5.0.7 on 2024-08-02 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
    ]
