# Generated by Django 4.2.13 on 2024-06-07 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario', '0004_alter_componentesequipo_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentesequipo',
            name='producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.producto'),
        ),
    ]