from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from flask import request

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=False, description='Admin status (true for admin)')
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=False, description='Admin status (true for admin)')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(403, 'Admin privileges required')
    @api.response(403, 'Admin privileges required')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        '''is_admin = user_data.get('is_admin', False)
        current_user = get_jwt_identity()

        # Prevent non-admins from creating admin users
        if is_admin:
            if not current_user or not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403'''
        '''is_admin = user_data.get('is_admin', False)
        current_user = get_jwt_identity()

        # Prevent non-admins from creating admin users
        if is_admin:
            if not current_user or not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403'''
        try:
            new_user = facade.create_user(user_data)
            return new_user.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of users"""
        users = facade.get_users()
        return [user.to_dict() for user in users], 200
    
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'User not found')
    @jwt_required()
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        """Modify user information"""
        try:
            current_user = get_jwt_identity()
            
            if str(user_id) != current_user:
                return {'error': 'Unauthorized action'}, 403
            
            user = facade.get_user(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            user_data = api.payload
            if 'email' in user_data or 'password' in user_data:
                return {'error': 'You cannot modify email or password'}, 400
            
            updated_user = facade.update_user(user_id, user_data)
            return updated_user.to_dict(), 200
        
        except ValueError as e:
        """Modify user information"""
        try:
            current_user = get_jwt_identity()
            
            if str(user_id) != current_user:
                return {'error': 'Unauthorized action'}, 403
            
            user = facade.get_user(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            user_data = api.payload
            if 'email' in user_data or 'password' in user_data:
                return {'error': 'You cannot modify email or password'}, 400
            
            updated_user = facade.update_user(user_id, user_data)
            return updated_user.to_dict(), 200
        
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'Failed to update user'}, 500