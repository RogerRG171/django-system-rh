# Generated by Django 4.1.3 on 2022-11-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa_nicho_mercado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnologia', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo_empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design')], max_length=3),
        ),
        migrations.AddField(
            model_name='empresa',
            name='tecnologias',
            field=models.ManyToManyField(to='empresa.tecnologias'),
        ),
    ]
