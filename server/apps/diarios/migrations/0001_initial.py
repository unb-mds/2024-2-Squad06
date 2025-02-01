# Generated by Django 4.1.13 on 2025-02-01 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_mensal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_anual', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vigencia', models.CharField(blank=True, max_length=100, null=True)),
                ('data_assinatura', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('excerpts', models.TextField(blank=True, null=True)),
                ('txt_url', models.URLField(blank=True, null=True)),
                ('contratacoes', models.ManyToManyField(blank=True, null=True, related_name='contratacao', to='diarios.contratacao')),
            ],
        ),
        migrations.AddField(
            model_name='contratacao',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='diarios.fornecedor'),
        ),
    ]
