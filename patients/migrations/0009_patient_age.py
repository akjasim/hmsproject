# Generated by Django 2.2.6 on 2019-11-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20191109_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
