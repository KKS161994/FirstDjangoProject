from django.contrib.auth.models import User
from rest_framework import serializers

from TestAPIAuths.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','snippets')