# Generated by Django 5.0.7 on 2024-08-02 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.CharField(blank=True, max_length=255)),
                ('house_number', models.CharField(blank=True, max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
            preserve_default=False,
        ),
    ]
