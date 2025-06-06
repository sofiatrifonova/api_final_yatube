import pytest

from posts.group import Group
from posts.models import Follow

from posts.models import Comment, Post


@pytest.fixture
def group_1():
    return Group.objects.create(title='Группа 1', slug='group_1')


@pytest.fixture
def group_2():
    return Group.objects.create(title='Группа 2', slug='group_2')


@pytest.fixture
def post(user, group_1):
    return Post.objects.create(
        text='Тестовый пост 1', author=user, group=group_1
    )


@pytest.fixture
def post_2(user, group_1):
    return Post.objects.create(
        text='Тестовый пост 12342341', author=user, group=group_1
    )


@pytest.fixture
def comment_1_post(post, user):
    return Comment.objects.create(author=user, post=post, text='Коммент 1')


@pytest.fixture
def comment_2_post(post, another_user):
    return Comment.objects.create(
        author=another_user, post=post, text='Коммент 2'
    )


@pytest.fixture
def another_post(another_user, group_2):
    return Post.objects.create(
        text='Тестовый пост 2', author=another_user, group=group_2
    )


@pytest.fixture
def comment_1_another_post(another_post, user):
    return Comment.objects.create(
        author=user, post=another_post, text='Коммент 12'
    )


@pytest.fixture
def follow_1(user, another_user):
    return Follow.objects.create(user=user, following=another_user)


@pytest.fixture
def follow_2(user_2, user):
    return Follow.objects.create(user=user_2, following=user)


@pytest.fixture
def follow_3(user_2, another_user):
    return Follow.objects.create(user=user_2, following=another_user)


@pytest.fixture
def follow_4(another_user, user):
    return Follow.objects.create(user=another_user, following=user)


@pytest.fixture
def follow_5(user_2, user):
    return Follow.objects.create(user=user, following=user_2)
