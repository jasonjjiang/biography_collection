# Generated by Django 4.2.4 on 2023-08-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='status',
            field=models.CharField(default='Finished reading', max_length=100),
            preserve_default=False,
        ),
    ]
