# Generated by Django 4.2.5 on 2023-10-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(),
        ),
    ]
