from flask_restful import Resource
from authz.controller import UserController


class UserResource(Resource):

    def get(self, user_id=None):
        if user_id is None:
            # Get users list
            return UserController.get_users()
        else:
            # get singel user
            return UserController.get_user(user_id)

    def post(self):
        # Create new user
        return UserController.create_user()

    def patch(self, user_id):
        # Update user
        return UserController.update_user(user_id)

    def delete(self, user_id):
        # Delete user
        return UserController.delete_user(user_id)
