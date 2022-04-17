# Generated by Django 4.0.3 on 2022-04-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_entity_entity_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roadmap',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]