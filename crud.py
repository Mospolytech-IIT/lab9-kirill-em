"""Импорт"""
from update_data import update_user_email as update_user_email_db, update_post_content
from delete_data import delete_user_and_posts, delete_post # pylint: disable=unused-import
from add_to_db import add_user, add_post
from extract_from_db import get_all_users, get_all_posts_with_users, get_posts_by_user

def create_user(username: str, email: str, password: str):
    """Создать юзера"""
    return add_user(username, email, password)

def create_post(title: str, content: str, user_id: int):
    """Создать пост"""
    return add_post(title, content, user_id)

def read_all_users():
    """Вывести всех юзеров"""
    return get_all_users()

def read_all_posts_with_users():
    """Вывести все посты"""
    return get_all_posts_with_users()

def read_posts_by_user(user_id):
    """Вывести все посты юзера"""
    return get_posts_by_user(user_id)

def update_user_email(user_id, new_email):
    """Обновить почту"""
    return update_user_email_db(user_id, new_email)

def update_post_content_db(post_id, new_content):
    """Обновить содержание поста"""
    return update_post_content(post_id, new_content)
