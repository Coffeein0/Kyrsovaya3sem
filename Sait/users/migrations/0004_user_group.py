# Generated by Django 5.1.1 on 2024-11-11 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.TextField(blank=True, null=True),
        ),
    ]