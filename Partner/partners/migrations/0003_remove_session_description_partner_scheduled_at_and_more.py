# Generated by Django 5.1.2 on 2024-11-30 15:13

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_remove_partner_status_alter_request_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='description',
        ),
        migrations.AddField(
            model_name='partner',
            name='scheduled_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='request',
            name='scheduled_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='partner',
            unique_together={('user', 'partner')},
        ),
    ]
