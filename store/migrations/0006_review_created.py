# Generated by Django 3.0.8 on 2020-07-16 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]