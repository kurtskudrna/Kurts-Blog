# Generated by Django 3.2.6 on 2021-08-04 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20210803_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='myblog.post')),
            ],
        ),
    ]
