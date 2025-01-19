# Generated by Django 4.1.13 on 2025-01-19 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='anual_valor',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='mensal_valor',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='vigencia',
        ),
        migrations.CreateModel(
            name='Contratacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensal_valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('anual_valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vigencia', models.CharField(blank=True, max_length=100, null=True)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratacoes', to='diarios.diario')),
            ],
        ),
    ]
