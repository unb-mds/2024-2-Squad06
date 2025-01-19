# Generated by Django 4.1.13 on 2025-01-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diarios', '0003_rename_anual_valor_contratacao_valor_anual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacao',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='diarios.fornecedor'),
        ),
    ]
