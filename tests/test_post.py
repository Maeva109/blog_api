from django.test import TestCase

import pytest
from blog_api.posts.models import Post
from blog_api.users.models import User

def test_create_user():
    user = User(name="John Doe", email="john.doe@example.com")
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"

def test_create_post():
    user = User(name="John Doe", email="john.doe@example.com")
    post = Post(title="My First Post", content="Content of the post", author=user)
    assert post.title == "My First Post"
    assert post.content == "Content of the post"
    assert post.author == user



