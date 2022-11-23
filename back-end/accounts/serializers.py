# accounts/serializers.py

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: 
    nickname = serializers.CharField(max_length=10)
    id = serializers.IntegerField(read_only=True)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['id'] = self.validated_data.get('id','')
        return data

class AccountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','username','nickname')

# <project_name>/settings.py

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
# }
