from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, first_name='', last_name='', phone=''):
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)

        user = self.model(
            email=self.normalize_email(email),
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.last_name = last_name
        user.first_name = first_name
        user.phone = phone
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        :param email: Email
        :param password: Password
        :return: User object
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'%s__iexact' % self.model.USERNAME_FIELD: username})
