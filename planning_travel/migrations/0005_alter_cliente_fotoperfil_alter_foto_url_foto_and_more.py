# Generated by Django 4.2.7 on 2023-11-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_travel', '0004_alter_cliente_fotoperfil_alter_foto_url_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fotoPerfil',
            field=models.ImageField(upload_to='planning_travel/media/'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='url_foto',
            field=models.ImageField(upload_to='planning_travel/media/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(upload_to='planning_travel/media/'),
        ),
    ]