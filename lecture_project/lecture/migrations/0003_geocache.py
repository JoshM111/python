# Generated by Django 2.2 on 2020-09-25 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_auto_20200922_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geocache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('treasure', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dragon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_geocaches', to='lecture.Dragon')),
            ],
        ),
    ]
