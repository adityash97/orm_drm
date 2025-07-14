from rest_framework.serializers import ModelSerializer
from .models import Users



class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields='__all__'
        extra_kwargs={
                        'password':{'write_only':True},
                        'password2':{'write_only':True}
                      }