# Generated by Django 3.1.7 on 2021-02-25 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wezom', '0003_auto_20210225_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostauto',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wezom.brand'),
        ),
        migrations.AlterField(
            model_name='lostauto',
            name='model',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wezom.model'),
        ),
    ]
