from .models import CustomUser
from django import forms


class EmailAuthBackend(object):
    """
    Authenticate using e-mail account.
    """

    def authenticate(self, email=None, password=None, role=None):
        user = CustomUser.get_by_email(email=email)
        if user is None:
            raise forms.ValidationError('Неккоректний адрес електронної пошти')
        if str(user.role) != role:
            raise forms.ValidationError('Неккоректна роль для цього аккаунту')
        if not user.check_password(password):
            raise forms.ValidationError('Неккоректний пароль')
        return user

    def get_user(self, user_id):
        return CustomUser.get_by_id(user_id)
