# Generated by Django 2.1.1 on 2018-12-24 17:12

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ranking_id',
            field=models.CharField(default=user.models.ranking_id_generator, max_length=60, verbose_name='id'),
        ),
    ]