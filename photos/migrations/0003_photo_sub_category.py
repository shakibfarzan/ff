# Generated by Django 4.0.6 on 2022-09-09 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_subcategory'),
        ('photos', '0002_alter_photo_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory'),
        ),
    ]
