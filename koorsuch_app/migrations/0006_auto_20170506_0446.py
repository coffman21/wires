# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koorsuch_app', '0005_auto_20170506_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spec',
            name='climate',
            field=models.CharField(choices=[('ND', 'Not Defined'), ('У', 'Умеренный климат'), ('ХЛ', 'Холодный климат'), ('УХЛ', 'Умеренный и холодный климат'), ('Т', 'Тропический климат'), ('М', 'Морской умеренно-холодный климат'), ('О', 'Общеклиматическое исполнение'), ('ОМ', 'Общеклиматическое морское исполнение'), ('В', 'Всеклиматическое исполнение')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spec',
            name='shape',
            field=models.CharField(blank=True, choices=[('', 'Круглые'), ('П', 'Плоские')], default='E', max_length=50),
        ),
    ]
