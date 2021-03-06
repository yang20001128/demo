# Generated by Django 3.2.4 on 2021-06-30 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='名称')),
                ('Gender', models.IntegerField(choices=[(1, '男性'), (2, '女性'), (3, '未定')], default=3, verbose_name='性别')),
                ('Born_Date', models.DateField(verbose_name='出生日期')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=100, verbose_name='书名')),
                ('Publish_Date', models.DateField(verbose_name='发布时间')),
                ('Country', models.CharField(max_length=100, verbose_name='国家')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo01.book')),
            ],
        ),
    ]
