import os
import django
import random
from faker import Faker
from datetime import timedelta
from django.utils import timezone



from ..models import Restaurant, Rating, Sale
from django.contrib.auth.models import User

fake = Faker()

def run():
    Faker.seed(42)
    random.seed(42)

    # Clear existing data (optional)
    Restaurant.objects.all().delete()
    Rating.objects.all().delete()
    Sale.objects.all().delete()
    User.objects.all().delete()

    # Create Users
    users = [
        User.objects.create_user(username=f"user{i}", email=f"user{i}@example.com", password="password")
        for i in range(1, 50)
    ]

    # Restaurant Types
    restaurant_types = [choice[0] for choice in Restaurant.TypeChoices.choices]

    restaurants = []
    for i in range(1, 100):
        restaurant = Restaurant.objects.create(
            name=fake.unique.company().title(),
            website=fake.url(),
            open_time=fake.time(),
            date_opened=fake.date_between(start_date="-10y", end_date="today"),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            restaurant_type=random.choice(restaurant_types),
        )
        restaurants.append(restaurant)

    # Create Ratings
    for _ in range(500):
        Rating.objects.create(
            user=random.choice(users),
            restaurant=random.choice(restaurants),
            rating=random.randint(1, 5)
        )

    # Create Sales
    for _ in range(1000):
        Sale.objects.create(
            restaurant=random.choice(restaurants),
            income=round(random.uniform(100.00, 10000.00), 2),
            datetime=timezone.now() - timedelta(days=random.randint(1, 365))
        )

    print("✅ Successfully populated 100+ entries in each model!")
