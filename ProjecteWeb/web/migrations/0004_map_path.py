# Generated by Django 5.1.6 on 2025-04-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_agent_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
