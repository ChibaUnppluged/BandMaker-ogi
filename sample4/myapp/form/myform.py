from django.forms import ModelForm
from myapp.models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user_name','password','birthday']