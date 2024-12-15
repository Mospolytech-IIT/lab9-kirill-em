# pylint: disable=line-too-long
"""Импорт"""
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from crud import (
    create_user, create_post,
    read_all_users, read_all_posts_with_users,
    update_user_email, update_post_content,
    delete_user_and_posts, delete_post
)

app = FastAPI()
templates = Jinja2Templates(directory="HTML")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Ссылки"""
    return """
    <p><a href="/users/new">Create User</a></p>
    <p><a href="/posts/new">Create Post</a></p>
    <p><a href="/users/list">List Users</a></p>
    <p><a href="/posts/list">List Posts</a></p>
    """

@app.get("/users/new", response_class=HTMLResponse)
async def create_user_form(request: Request):
    """Создать страницу юзера"""
    return templates.TemplateResponse("create_user.html", {"request": request})

@app.post("/users/")
async def api_create_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    """Создать юзера"""
    try:
        create_user(username=username, email=email, password=password)
        return RedirectResponse("/users/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {e}") from e

@app.get("/posts/new", response_class=HTMLResponse)
async def create_post_form(request: Request):
    """Создать страницу поста"""
    users = read_all_users()
    return templates.TemplateResponse("create_post.html", {"request": request, "users": users})

@app.post("/posts/")
async def api_create_post(title: str = Form(...), content: str = Form(...), user_id: int = Form(...)):
    """Создать пост"""
    try:
        create_post(title=title, content=content, user_id=user_id)
        return RedirectResponse("/posts/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating post: {e}") from e

@app.get("/users/list", response_class=HTMLResponse)
async def list_users(request: Request):
    """Списко пользователей"""
    users = read_all_users()
    return templates.TemplateResponse("list_users.html", {"request": request, "users": users})

@app.get("/posts/list", response_class=HTMLResponse)
async def list_posts(request: Request):
    """Список постов"""
    posts = read_all_posts_with_users()
    return templates.TemplateResponse("list_posts.html", {"request": request, "posts": posts})

@app.get("/users/edit/{user_id}", response_class=HTMLResponse)
async def edit_user_form(request: Request, user_id: int):
    """Страница редакторивания юзера"""
    user = next((u for u in read_all_users() if u.id == user_id), None)
    if user:
        return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/edit/{user_id}")
async def api_edit_user(user_id: int, email: str = Form(...)):
    """Редактирование юзера"""
    try:
        update_user_email(user_id, email)
        return RedirectResponse("/users/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user: {e}") from e

@app.post("/users/delete/{user_id}")
async def api_delete_user(user_id: int):
    """Удаление юзера"""
    try:
        delete_user_and_posts(user_id)
        return RedirectResponse("/users/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting user: {e}") from e

@app.post("/posts/delete/{post_id}")
async def api_delete_post(post_id: int):
    """УЦдаление поста"""
    try:
        delete_post(post_id)
        return RedirectResponse("/posts/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting post: {e}") from e

@app.get("/posts/edit/{post_id}", response_class=HTMLResponse)
async def edit_post_form(request: Request, post_id: int):
    """Страница редактирования поста"""
    post = next((p for p in read_all_posts_with_users() if p.post_id == post_id), None)
    if post:
        return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/edit/{post_id}")
async def api_edit_post(post_id: int, content: str = Form(...)):
    """Реадктирование поста"""
    try:
        update_post_content(post_id, content)
        return RedirectResponse("/posts/list", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating post: {e}") from e
