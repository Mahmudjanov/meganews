# Generated by Django 4.2.5 on 2024-02-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_category_homecategory_single_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='HomeCategory',
        ),
    ]
