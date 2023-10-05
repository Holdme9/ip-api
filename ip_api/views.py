from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import IPModelSerializer
from .permissions import EvenIPPermission

from .models import IPAPIModel
from .funcs import get_client_ip_address


class ModelCreateAPIView(CreateAPIView):
    """An API to create IP Model objects."""
    serializer_class = IPModelSerializer


class ModelRUDAPIView(RetrieveUpdateDestroyAPIView):
    """An API to perform RUD operations for IP Model.
    Only allowed for client's with specific permission."""
    queryset = IPAPIModel.objects.all()
    serializer_class = IPModelSerializer
    permission_classes = [EvenIPPermission]


class GetIPAPIView(APIView):
    """An API that returns client's IP in JSON."""
    def get(self, request):
        ip = get_client_ip_address(request)
        data = {'ip': ip}
        return Response(data, status=status.HTTP_200_OK)
