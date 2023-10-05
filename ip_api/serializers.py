from rest_framework.serializers import ModelSerializer

from ip_api.models import IPAPIModel


class IPModelSerializer(ModelSerializer):
    """Serializer for IP Model."""
    class Meta:
        model = IPAPIModel
        fields = '__all__'
