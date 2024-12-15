"""Импорт"""
from sqlalchemy.orm import sessionmaker
from database import User, Post, engine

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username: str, email: str, password: str):
    """Добавление юзера"""
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def add_post(title: str, content: str, user_id: int):
    """Добавление поста"""
    post = Post(title=title, content=content, user_id=user_id)
    session.add(post)
    session.commit()
    return post
