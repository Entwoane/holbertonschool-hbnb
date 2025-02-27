from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        user.update(**user_data)
        self.user_repo.update(user_id, user)
        return user

    def create_amenity(self, amenity_data):
        if not amenity_data or 'name' not in amenity_data:
            return None

        new_amenity = Amenity(amenity_data["name"])
        self.amenity_repo.add(new_amenity)

        print(f">>> Amenity created: {new_amenity.id}")

        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        print(f">>> Searching for Amenity ID {amenity_id}: Found? {amenity is not None}")
        return amenity

    def get_all_amenities(self):
        amenities = self.amenity_repo.get_all()
        return [a.to_dict() for a in amenities]

    def update_amenity(self, amenity_id, data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        
        print(f">>> Type de data reçu dans update_amenity(): {type(data)} - Contenu: {data}")

        if not isinstance(data, dict):
            raise TypeError(f"Expected 'data' to be a dict, got {type(data)} instead.")
        
        new_name = data.get("name")
        print(f">>> new_name extrait de data: {data.get('name')} (type: {type(data.get('name'))})")

        if not isinstance(new_name, str):
            raise TypeError("new_name must be a string")

        amenity.update({"name": new_name})
        self.amenity_repo.update(amenity_id, {"name": new_name})

        return amenity

facade = HBnBFacade()