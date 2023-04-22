# Generated by Django 4.1.7 on 2023-04-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_room_is_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: text. Name of the Document', max_length=75, verbose_name='Document Name')),
                ('description', models.TextField(help_text='format: text. Write a description of the associated file!', verbose_name='File Description')),
                ('file', models.FileField(help_text='format: txt, pdf, img, png. jpg, jpeg, audio. Upload your intented file', upload_to='Files/%Y/%M/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]