# Generated by Django 2.0.7 on 2019-02-20 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0014_oauthapp'),
        ('oauth2_provider', '0007_auto_20190214_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='app',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oauth_app', to='oneid_meta.APP'),
        ),
        migrations.AlterField(
            model_name='application',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], default='authorization-code', max_length=32),
        ),
        migrations.AlterField(
            model_name='application',
            name='client_type',
            field=models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], default='confidential', max_length=32),
        ),
    ]
