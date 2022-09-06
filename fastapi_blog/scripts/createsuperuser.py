from fastapi_blog.db.database import SessionLocal
from fastapi_blog.db.base import User
from fastapi_blog.user.security import get_password_hash

from sqlalchemy.orm import Session


def main():
    db: Session = SessionLocal()
    username = input('username: ')
    password = input('password: ')
    email = input('email: ')

    user_check = db.query(User).filter(User.username == username).first()
    if not user_check:
        password_hash = get_password_hash(password)
        user = User(
            username=username,
            password=password_hash,
            email=email,
            is_active=True,
            is_admin=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print('Success')
    else:
        print('Error, user existing')
    db.close()


if __name__ == "__main__":
    main()
