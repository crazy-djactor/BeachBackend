# Generated by Django 3.0.7 on 2020-07-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200701_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beach',
            name='location_coord',
            field=models.TextField(default='{}', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='beach',
            name='location_degree',
            field=models.TextField(default='{}', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='location_coord',
            field=models.TextField(default='{}', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='location_degree',
            field=models.TextField(default='{}', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='traffic_level',
            field=models.TextField(default='{}', max_length=255, null=True),
        ),
    ]
