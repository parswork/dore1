# Example migration file
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Add any dependencies here
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('ncode' , models.CharField(max_length=10)),
                ('phonenumber',models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('arr', models.CharField(max_length=100)),
            ],
        ),
    ]
