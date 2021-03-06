# Generated by Django 2.1.1 on 2018-09-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20180913_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistsraw',
            name='likes',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='artistsraw',
            name='loc_lat',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='artistsraw',
            name='loc_long',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='artistsraw',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
