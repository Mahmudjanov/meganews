# Generated by Django 4.2.5 on 2024-02-18 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_single'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
