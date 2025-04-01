from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.group import Group
from posts.models import Follow

from posts.models import Comment, Post


class GroupSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(
    serializers.ModelSerializer
):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)

    def validate(self, data):
        user = self.context['request'].user
        following = data.get('following')

        if user == following:
            raise serializers.ValidationError("Нельзя подписаться на себя")

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError("Вы уже подписаны")

        return data


class PostSerializer(
    serializers.ModelSerializer
):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    pub_date = serializers.DateTimeField(
        read_only=True,
        required=False
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author',
                  'group', 'pub_date', 'image')
        read_only_fields = ('author', 'pub_date',)


class CommentSerializer(
    serializers.ModelSerializer
):
    author = serializers.StringRelatedField(
        read_only=True,
        required=False,
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
        required=False,
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author',
                  'post', 'created')
        read_only_fields = ('author', 'post',)
