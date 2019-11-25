# Generated by Django 2.2.6 on 2019-11-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('availability', models.IntegerField(help_text='Specify in bottles.')),
            ],
        ),
    ]
