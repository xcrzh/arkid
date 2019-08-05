# Generated by Django 2.0.7 on 2019-07-16 07:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0039_auto_20190712_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('subject', models.CharField(default='', max_length=128, verbose_name='类型')),
                ('summary', models.CharField(default='', max_length=512, verbose_name='事件信息')),
            ],
        ),
        migrations.CreateModel(
            name='RequestAccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='IP地址')),
                ('agent', models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='HTTP_USER_AGENT')),
                ('url', models.TextField(blank=True, default='', null=True, verbose_name='完整请求路径')),
                ('method', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='REQUEST_METHOD')),
            ],
        ),
        migrations.CreateModel(
            name='RequestDataClientLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='请求内容')),
                ('content_type', models.TextField(blank=True, default='', null=True, verbose_name='内容类型')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='access',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneid_meta.RequestAccessLog'),
        ),
        migrations.AddField(
            model_name='log',
            name='data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oneid_meta.RequestDataClientLog'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oneid_meta.User', verbose_name='操作者'),
        ),
    ]
