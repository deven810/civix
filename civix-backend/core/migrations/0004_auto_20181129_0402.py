# Generated by Django 2.1.3 on 2018-11-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181128_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='streetAddress',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='events',
            field=models.ManyToManyField(blank=True, to='core.Event'),
        ),
    ]
