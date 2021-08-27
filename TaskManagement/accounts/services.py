from accounts.models import User
from django.db.models import Q
from allauth.account.models import EmailAddress


class AccountManagement():
    def get_user(self, search, *args, **kwargs):
        """
        search user from the userlist according to name or username or email or designation
        """
        user_list = User.objects.filter(Q(username__icontains=search) |
                                        Q(email__icontains=search) |
                                        Q(first_name__icontains=search) |
                                        Q(designation__icontains=search)).order_by('-id')
        return user_list

    def set_email(self, userdata, *args, **kwargs):
        """
        store the data in EmailAddress model of created user using FK. 
        """
        userd = EmailAddress.objects.get_or_create(user=userdata,
                                                    email=userdata.email,
                                                    verified= True, 
                                                    primary= True)
        return userd
