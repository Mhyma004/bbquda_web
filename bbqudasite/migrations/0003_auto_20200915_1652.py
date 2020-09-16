# Generated by Django 3.1.1 on 2020-09-15 16:52

import bbqudasite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbqudasite', '0002_auto_20200914_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvupload',
            name='file',
            field=models.FileField(upload_to='media/csv/', validators=[bbqudasite.models.csv_file_validator]),
        ),
        migrations.AlterField(
            model_name='csvupload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]