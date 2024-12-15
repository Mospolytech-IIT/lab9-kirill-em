"""Импорт"""
from sqlalchemy.orm import sessionmaker
from database import User, Post, engine

Session = sessionmaker(bind=engine)
session = Session()

def get_all_users():
    """Вывод всех юзеров"""
    users = session.query(User).all()
    return users

def get_all_posts_with_users():
    """Вывод всех постов с юзерами"""
    posts = session.query(Post).all()
    result = []
    for post in posts:
        result.append({
            "post_id": post.id,
            "title": post.title,
            "content": post.content,
            "user": {
                "username": post.user.username,
                "email": post.user.email
            }
        })
    return result

def get_posts_by_user(user_id):
    """Вывести все посты юзера"""
    posts = session.query(Post).filter_by(user_id=user_id).all()
    result = []
    for post in posts:
        result.append({
            "post_id": post.id,
            "title": post.title,
            "content": post.content
        })
    return result
