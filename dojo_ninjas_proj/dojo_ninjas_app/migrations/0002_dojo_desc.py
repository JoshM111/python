# Generated by Django 2.2 on 2020-09-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='new!'),
            preserve_default=False,
        ),
    ]
