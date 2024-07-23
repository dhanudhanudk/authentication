from rest_framework import serializers,validators
from django.contrib.auth.models import User
from.models import*
from rest_framework.validators import UniqueValidator

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','username','password']

        def create(self,validated_data):
            user=User(
                username=validated_data['username'],
                password=validated_data['password']
            )
            user.save()
            return user
       

    # ## model serializers
class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = '__all__'
        extra_kwargs ={
            'password':{"write_only":True},
            'email': {
            'validators': [
                validators.UniqueValidator(
                    SampleData.objects.all(),"This Email Already Exists"
                )
            ]
        }
    }
       