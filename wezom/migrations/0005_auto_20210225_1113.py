# Generated by Django 3.1.7 on 2021-02-25 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wezom', '0004_auto_20210225_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostauto',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wezom.brand'),
        ),
        migrations.AlterField(
            model_name='lostauto',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wezom.model'),
        ),
    ]
