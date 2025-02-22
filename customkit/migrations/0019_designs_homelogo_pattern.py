# Generated by Django 5.0.1 on 2024-09-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0018_remove_customfonts_google_fonts_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='designs')),
            ],
        ),
        migrations.CreateModel(
            name='HomeLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='patterns')),
            ],
        ),
    ]
