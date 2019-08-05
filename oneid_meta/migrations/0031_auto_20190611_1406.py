# Generated by Django 2.0.7 on 2019-06-11 06:06

from django.db import migrations, models
import jsonfield.fields
import uuid


def init_user_native_field(apps, schema_editor):
    '''
    初始化user字段
    '''
    NativeField = apps.get_model('oneid_meta', 'NativeField')

    NativeField.objects.create(name='姓名', key='name', is_visible_editable=False)
    NativeField.objects.create(name='邮箱', key='email', is_visible_editable=False)
    NativeField.objects.create(name='部门', key='depts',
        schema={'type': 'array', 'items': {
            'type': 'object',
            'properties': {
                'uid': {'type': 'string'},
                'name': {'type': 'string'},
            },
        }},
        is_visible_editable=False)
    NativeField.objects.create(name='手机', key='mobile')
    NativeField.objects.create(name='工号', key='employee_number')
    NativeField.objects.create(name='性别', key='gender', schema={'type': 'interger'})


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0030_customfield_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NativeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128, verbose_name='字段名称')),
                ('key', models.CharField(max_length=256, verbose_name='内部字段名')),
                ('subject', models.CharField(choices=[('user', '用户')], default='user', max_length=128, verbose_name='字段分类')),
                ('schema', jsonfield.fields.JSONField(default={'type': 'string'}, verbose_name='字段定义')),
                ('is_visible', models.BooleanField(default=True, verbose_name='是否展示')),
                ('is_visible_editable', models.BooleanField(default=True, verbose_name='对于`是否展示`，是否可以修改')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customfield',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='是否展示'),
        ),
        migrations.RunPython(init_user_native_field),
    ]
