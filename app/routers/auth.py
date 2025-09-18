from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.services.oauth_service import oauth2_service
from app.services.auth_service import AuthService
from app.schemas.auth import TokenResponse, UserResponse
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.db import get_db  # Your existing database dependency

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.get("/login")
async def login(request: Request):
    """Redirect to Google OAuth2 login"""
    google = oauth2_service.get_google_client()
    redirect_uri = request.url_for('auth_callback')
    return await google.authorize_redirect(request, redirect_uri)

@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Google OAuth2 callback"""
    try:
        google = oauth2_service.get_google_client()
        token = await google.authorize_access_token(request)
        user_info = token.get('userinfo')
        
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to get user info from Google"
            )
        
        auth_service = AuthService(db)
        user = auth_service.authenticate_or_create_user(user_info)
        access_token = auth_service.create_access_token_for_user(user)
        
        # In a real app, you might want to redirect to frontend with token
        # For now, we'll return the token
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse.from_orm(user)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Authentication failed: {str(e)}"
        )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information"""
    return UserResponse.from_orm(current_user)

@router.post("/logout")
async def logout():
    """Logout endpoint (client should discard token)"""
    return {"message": "Successfully logged out"}
