# Generated by Django 2.0.2 on 2018-02-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_course', '0002_course_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True)),
                ('git_origin', models.CharField(default='', max_length=255)),
                ('git_branch', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('owner', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
