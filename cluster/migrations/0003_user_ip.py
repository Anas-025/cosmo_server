# Generated by Django 5.0.2 on 2024-03-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0002_remove_comet_name_comet_type_of_comet'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip',
            field=models.CharField(default='0.0.0.0', max_length=200),
            preserve_default=False,
        ),
    ]