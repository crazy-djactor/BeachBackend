# Generated by Django 3.0.7 on 2020-07-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200701_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='beach',
            name='count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='light_state',
            field=models.IntegerField(null=True),
        ),
    ]
