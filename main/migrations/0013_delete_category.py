# Generated by Django 4.2.5 on 2024-02-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_posts_author_remove_posts_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
