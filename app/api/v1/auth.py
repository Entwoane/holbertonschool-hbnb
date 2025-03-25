from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload  # Get the email and password from the request payload
        print(f"\n--- Login Attempt ---")
        print(f"Raw input email: '{credentials['email']}'")
        print(f"Trimmed/lowered: '{credentials['email'].strip().lower()}'\n")
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])
        
        # Step 2: Check if the user exists and the password is correct
        if not user:
            print(f"User not found for email: {credentials['email']}")
            return {'error': 'Invalid credentials'}, 401
        if not user.verify_password(credentials['password']):
            print(f"Invalid password for user: {credentials['email']}")  # Debug log
            return {'error': 'Invalid credentials'}, 401
        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(identity={'id': str(user.id),
                                                     'is_admin': user.is_admin})
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200
