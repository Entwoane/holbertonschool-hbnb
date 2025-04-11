from flask import current_app
from app.extensions import db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

def init_db():
    """Initialize the database by creating tables."""
    db.create_all()
    
def seed_db():
    """Seeds the database with initial data if it doesn't exist."""
    _seed_admin_user()
    _seed_amenities()
    _seed_places()
    
    db.session.commit()

def _seed_admin_user():
    """Create the admin user if it doesn't exist."""
    admin_exists = User.query.filter_by(email=current_app.config['ADMIN_EMAIL']).first()
    
    if not admin_exists:
        admin = User(
            first_name=current_app.config['ADMIN_FIRST_NAME'],
            last_name=current_app.config['ADMIN_LAST_NAME'],
            email=current_app.config['ADMIN_EMAIL'],
            password=current_app.config['ADMIN_PASSWORD'],
            is_admin=True
        )
        db.session.add(admin)
        current_app.logger.info(f"Admin user created: {admin.email}")
    else:
        current_app.logger.info("Admin user already exists.")

def _seed_amenities():
    """Create the initial amenities if they don't exist."""
    for amenity_name in current_app.config['INITIAL_AMENITIES']:
        if not Amenity.query.filter_by(name=amenity_name).first():
            amenity = Amenity(
                name=amenity_name
            )
            db.session.add(amenity)
            current_app.logger.info(f"Amenity created: {amenity.name}")
        else:
            current_app.logger.info(f"Amenity already exists: {amenity_name}")

def _seed_places():
    """Seed the database with initial places if they don't already exist."""

    if Place.query.count() > 0:
        current_app.logger.info("Places already exist. Skipping seeding.")
        return


    admin = User.query.filter_by(email=current_app.config['ADMIN_EMAIL']).first()
    if not admin:
        current_app.logger.error("Admin user not found. Cannot seed places.")
        return

    wifi = Amenity.query.filter_by(name='WiFi').first()
    pool = Amenity.query.filter_by(name='Swimming Pool').first()
    ac = Amenity.query.filter_by(name='Air Conditioning').first()


    sample_places = [
        {
            "title": "Urban Loft in the Heart of Downtown",
            "description": "Modern loft with stylish decor, large windows, and city skyline views. Located steps away from restaurants, shops, and nightlife. Ideal for business travelers or weekend explorers.",
            "price": 150.00,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "amenities": [wifi, ac]  
        },
        {
            "title": "Cozy Mountain Retreat with Stunning Views",
            "description": "Charming cabin with breathtaking views, a fireplace, and access to hiking trails. Features 2 bedrooms, a full kitchen, and a private deck for stargazing. Perfect for a peaceful getaway or outdoor adventure.",
            "price": 300.00,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "amenities": [wifi]  
        },
        {
            "title": "Beachfront Bungalow with Private Deck",
            "description": "Relax in this cozy beachfront bungalow featuring ocean views, a private deck, and direct beach access. Perfect for couples or solo travelers seeking a tranquil seaside escape.",
            "price": 200.00,
            "latitude": 51.5074,
            "longitude": -0.1278,
            "amenities": [pool, ac, wifi]  
        }
    ]

    for place_data in sample_places:
        place = Place(
            title=place_data["title"],
            description=place_data["description"],
            price=place_data["price"],
            latitude=place_data["latitude"],
            longitude=place_data["longitude"],
            owner=admin  
        )
        place.amenities.extend(place_data["amenities"])  
        db.session.add(place)
        current_app.logger.info(f"Place created: {place.title}")

    current_app.logger.info("Successfully seeded places.")