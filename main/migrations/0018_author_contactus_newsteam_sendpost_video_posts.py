# Generated by Django 4.2.5 on 2024-02-19 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_contactus_delete_newsteam_remove_posts_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('addfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewsTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SendPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('video_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('views', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
