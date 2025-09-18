from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.services.jwt_service import JWTService
from app.models.user import User
from typing import Optional

class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
        self.jwt_service = JWTService()
    
    def authenticate_or_create_user(self, user_info: dict) -> User:
        """Authenticate existing user or create new one from Google OAuth data"""
        google_id = user_info.get('sub')
        email = user_info.get('email')
        
        # Try to find existing user
        user = self.user_repo.get_user_by_google_id(google_id)
        
        if not user:
            # Create new user
            user_data = {
                'email': email,
                'full_name': user_info.get('name'),
                'google_id': google_id,
                'profile_picture': user_info.get('picture'),
                'is_active': True
            }
            user = self.user_repo.create_user(user_data)
        else:
            # Update existing user info
            update_data = {
                'full_name': user_info.get('name'),
                'profile_picture': user_info.get('picture'),
            }
            user = self.user_repo.update_user(user, update_data)
        
        return user
    
    def create_access_token_for_user(self, user: User) -> str:
        token_data = {"sub": str(user.id), "email": user.email}
        return self.jwt_service.create_access_token(token_data)
    
    def get_current_user(self, token: str) -> Optional[User]:
        """Get current user from JWT token"""
        payload = self.jwt_service.verify_token(token)
        if not payload:
            return None
        
        user_id = payload.get("sub")
        if not user_id:
            return None
            
        return self.user_repo.get_user_by_id(int(user_id))
