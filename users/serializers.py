

from rest_framework import serializers

from users.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):

    user_id=serializers.ReadOnlyField()
    class Meta:
        model=User
        fields='__all__'