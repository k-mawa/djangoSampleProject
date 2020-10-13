# Generated by Django 3.1.1 on 2020-10-13 09:02

from django.db import migrations, models
import django.utils.timezone
import usermanager.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('mysiteUrl1', models.URLField(blank=True, null=True, verbose_name='mysiteUrl1')),
                ('mysiteUrl2', models.URLField(blank=True, null=True, verbose_name='mysiteUrl2')),
                ('introduction_of_user', models.TextField(blank=True, null=True)),
                ('postal_num', models.CharField(blank=True, max_length=150, null=True)),
                ('address_one', models.CharField(blank=True, choices=[('その他', 'その他'), ('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('群馬県', '群馬県'), ('栃木県', '栃木県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('山梨県', '山梨県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('長野県', '長野県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('滋賀県', '滋賀県'), ('岐阜県', '岐阜県'), ('三重県', '三重県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('高知県', '高知県'), ('愛媛県', '愛媛県'), ('鳥取県', '鳥取県'), ('岡山県', '岡山県'), ('島根県', '島根県'), ('広島県', '広島県'), ('山口県', '山口県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('大分県', '大分県'), ('熊本県', '熊本県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=50, null=True)),
                ('address_two', models.CharField(blank=True, max_length=150, null=True)),
                ('address_three', models.CharField(blank=True, max_length=150, null=True)),
                ('tel_one', models.CharField(blank=True, max_length=150, null=True)),
                ('tel_two', models.CharField(blank=True, max_length=150, null=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', usermanager.models.UserManager()),
            ],
        ),
    ]