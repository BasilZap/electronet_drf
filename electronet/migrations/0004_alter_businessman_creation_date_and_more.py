# Generated by Django 5.0 on 2024-01-02 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronet', '0003_alter_businessman_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessman',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 2, 21, 48, 8, 150756), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 2, 21, 48, 8, 150756), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 2, 21, 48, 8, 149755), null=True, verbose_name='Дата создания'),
        ),
    ]
