
# Generated by Django 4.1 on 2022-11-27 23:31


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_alter_author_options_alter_author_books_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-id'], 'permissions': [('read_author', 'Can read author')], 'verbose_name': 'автор(а)', 'verbose_name_plural': 'автори(ів)'},
        ),
    ]
