# Generated by Django 3.1.7 on 2021-02-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20210226_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='is_mvp',
            field=models.BinaryField(default=0),
        ),
    ]