# Generated by Django 4.2.14 on 2024-07-18 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='booking',
            name='table_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'table_number')},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
