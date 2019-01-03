from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):

        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['email'].label = "Email"

