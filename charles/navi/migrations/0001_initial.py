# Generated by Django 2.2.3 on 2020-07-25 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='类目标题', max_length=64)),
                ('html_id', models.CharField(help_text='类目ID', max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='网址标题', max_length=64)),
                ('description', models.CharField(default='这里还没什么描述', help_text='描述', max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('img_path', models.CharField(default='/', help_text='导航图片', max_length=255)),
                ('read_no', models.IntegerField(default=0, help_text='浏览数')),
                ('ordering', models.IntegerField(default=99, help_text='置顶')),
                ('cate', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='cates', to='navi.Category')),
            ],
        ),
    ]