from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UsuarioManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, name, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    nombre = models.CharField(max_length=60, blank=True)
    apellido = models.CharField(max_length=100, blank=True)  
    # medico = models.ForeignKey('Medico',null=True, blank=True, related_name='med_profiles')
    # consultorio = models.ForeignKey('Consultorio', null=True, blank=True, related_name='con_profiles', on_delete=models.PROTECT)
    tipo = models.PositiveSmallIntegerField(default=0)    
    genero_codigo = models.BooleanField(default=False)
    codigo_gen = models.IntegerField(null=True, blank=True)
    fecha_gen = models.DateField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=128)

    
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = "usuario"

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.name

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email


class StatusUpdate(models.Model):
    """A users status update."""

    user = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """A users message from one user to another."""

    sender = models.ForeignKey('Usuario', related_name='fk_message_sender')
    recipient = models.ForeignKey(
        'Usuario', related_name='fk_message_recipient')
    message = models.CharField(max_length=255)
    date_sent = models.DateTimeField(auto_now_add=True)