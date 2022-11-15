# Generated by Django 4.1.3 on 2022-11-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design'), ('JS', 'Javascript'), ('UI', 'User Iterface'), ('UX', 'User Experience'), ('JAV', 'Java'), ('SPR', 'Spring'), ('AND', 'Android'), ('RCT', 'React'), ('RTN', 'React Native'), ('ND', 'Node JS'), ('Py', 'Python'), ('DJG', 'Django'), ('MQL', 'Mysql')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
