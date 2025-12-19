

from rest_framework import serializers

from users.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url=serializers.HyperlinkedIdentityField(
    #     view_name='users-detail',
    #     lookup_field='user_id'
    # )

    user_id=serializers.ReadOnlyField()
    class Meta:
        model=User
        fields='__all__'