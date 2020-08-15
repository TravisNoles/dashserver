# Generated by Django 3.1 on 2020-08-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermgr', '0004_auto_20200814_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='operatingsystem',
            field=models.CharField(choices=[(167, 'CentOS7')], default=400, max_length=10),
        ),
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='server',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
