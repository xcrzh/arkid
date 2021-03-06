# Generated by Django 2.2.10 on 2020-04-17 07:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0072_auto_20200413_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrontabPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=255, verbose_name='插件名称')),
                ('detail', models.CharField(max_length=1024, verbose_name='插件详细描述')),
                ('import_path', models.CharField(max_length=1024, verbose_name='插件实现所在路径')),
                ('schedule', models.CharField(max_length=255, verbose_name='执行周期')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MiddlewarePlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=255, verbose_name='插件名称')),
                ('detail', models.CharField(max_length=1024, verbose_name='插件详细描述')),
                ('import_path', models.CharField(max_length=1024, verbose_name='插件实现所在路径')),
                ('order_no', models.IntegerField(default=0, verbose_name='排序号')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
