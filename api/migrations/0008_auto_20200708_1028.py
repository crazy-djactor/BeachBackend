# Generated by Django 3.0.7 on 2020-07-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200703_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]