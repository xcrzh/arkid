# Generated by Django 2.0.7 on 2019-01-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0008_auto_20190125_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinggroup',
            name='is_role_group',
            field=models.BooleanField(default=False, verbose_name='区分角色组与角色'),
        ),
    ]
