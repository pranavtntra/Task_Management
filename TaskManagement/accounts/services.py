from accounts.models import User
from django.db.models import Q


class AccountManagement():
    def get_user(self, search, *args, **kwargs):
        """
        search user from the userlist according to name or username or email or designation
        """
        user_list = User.objects.filter(Q(username__icontains=search) |
                                        Q(email__icontains=search) |
                                        Q(first_name__icontains=search) |
                                        Q(designation__icontains=search))
        return user_list
