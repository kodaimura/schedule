# Generated by Django 3.0.5 on 2020-04-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('S_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=4, verbose_name='年')),
                ('month', models.CharField(max_length=2, verbose_name='月')),
                ('day', models.CharField(max_length=2, verbose_name='日')),
                ('time', models.CharField(default='00:00', max_length=5, verbose_name='時')),
                ('task', models.CharField(max_length=30, verbose_name='予定')),
                ('details', models.TextField(blank=True, verbose_name='詳細')),
                ('importance', models.BooleanField(verbose_name='重要')),
            ],
        ),
    ]
