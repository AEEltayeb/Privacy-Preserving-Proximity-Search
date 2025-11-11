import math
# Create your views here.
from phe import paillier
import random
from .models import Location

def encrypt_diffs(x_value, y_value):
    public_key, private_key = paillier.generate_paillier_keypair()
    enc_user_x, enc_user_y = encrypting(x_value, y_value, public_key)
    encrypted_diffs = calculate_encrypted_diffs(enc_user_x, enc_user_y, public_key)
    activities_distances = []
    for data in encrypted_diffs:
        activity = data['activity']
        enc_diff_x = data['enc_diff_x']
        enc_diff_y = data['enc_diff_y']
        diff_x = private_key.decrypt(enc_diff_x)
        diff_y = private_key.decrypt(enc_diff_y)
        distance = math.sqrt(diff_x**2 + diff_y**2)
        activities_distances.append((activity, distance))

        # Sort by distance and get top 10
    activities_distances.sort(key=lambda x: x[1])
    top_activities = activities_distances[:10]

    return top_activities

def populate_locations():
    activities = ['Shawarma restaurant', 'Bowling', 'Rec center', 'Cafe', 'Park', 'heritage site']
    for i in range(100):
        activity = random.choice(activities)
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        Location.objects.create(activity=activity, x=x, y=y)

def encrypting(user_x, user_y, public_key):
    enc_user_x = public_key.encrypt(float(user_x))
    enc_user_y = public_key.encrypt(float(user_y))
    return enc_user_x, enc_user_y

def calculate_encrypted_diffs(enc_user_x, enc_user_y, public_key):
    # Retrieve locations from the database
    locations = Location.objects.all()
    encrypted_diffs = []
    for loc in locations:
        enc_diff_x = public_key.encrypt(loc.x) - enc_user_x
        enc_diff_y = public_key.encrypt(loc.y) - enc_user_y
        encrypted_diffs.append({
            'activity': loc.activity,
            'enc_diff_x': enc_diff_x,
            'enc_diff_y': enc_diff_y
        })

    return encrypted_diffs