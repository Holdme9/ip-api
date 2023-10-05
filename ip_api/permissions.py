from rest_framework import permissions
from .funcs import get_client_ip_address


class EvenIPPermission(permissions.BasePermission):
    """Checks if client has specific permission."""

    @staticmethod
    def compare_even_digits_to_odd(ip):
        """Checks if amount of even digits in IP
        equals to amount of odd digits."""
        even_digits = odd_digits = 0

        for char in ip:
            if not char.isdigit():
                continue
            elif int(char) % 2 == 0:
                even_digits += 1
            else:
                odd_digits += 1

        return even_digits == odd_digits

    def has_permission(self, request, view):
        """Returns True if client has specific permission."""
        ip = get_client_ip_address(request)
        return self.compare_even_digits_to_odd(ip)
