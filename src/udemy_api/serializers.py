from rest_framework import serializers

from udemy_api.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'name', 'is_active', 'is_staff', 'tipo', 'nombre', 
                    'apellido', 'genero_codigo', 'codigo_gen', 'fecha_gen', 'fecha_nacimiento',
                    'last_login', 'password', 'token')
        extra_kwargs = {
            'last_login': {'read_only': True},
            'genero_codigo': {'read_only': True},
            'codigo_gen': {'read_only': True},
            'fecha_gen': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Used to create a new user."""

        user = Usuario(
            email=validated_data['email'],
            name=validated_data['name'],
            is_active=validated_data['is_active'],            
            tipo=validated_data['tipo'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],            
            fecha_nacimiento=validated_data['fecha_nacimiento'],
            # pw=validated_data['password']
            
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
