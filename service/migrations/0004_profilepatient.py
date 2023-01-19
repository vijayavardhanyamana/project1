# Generated by Django 4.1.4 on 2022-12-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_login_login1'),
    ]

    operations = [
        migrations.CreateModel(
            name='profilepatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('bloodgroup', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('dateofbirth', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
