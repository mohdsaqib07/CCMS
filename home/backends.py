# You should create the backends.py file in your Django app's directory. This is because the custom authentication backend is specific to your app and extends the default authentication system provided by Django. Placing it in the app's directory helps keep your project organized and ensures that the custom backend is only used within that app.
from django.db.models import Q
from django.contrib.auth import get_user_model
# ModelBackend is the base class for dja0-ngo authentication models
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
