# Generated by Django 5.2 on 2025-04-13 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('tipo_documento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Documento')),
                ('numero_documento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de Documento')),
                ('imagen', models.ImageField(blank=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
            ],
        ),
    ]
