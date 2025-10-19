import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leaderboard_api.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "bkay"
email = "bkay@demo.com"
password = "demo@1234"  # temporary password for demo purposes only to change asap

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created successfully!")
else:
    print("⚠️ Superuser already exists.")
