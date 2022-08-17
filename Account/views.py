from django.shortcuts import render,redirect
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import  UserCreationForm
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import User,AccUser, Voter,candidate,Election_Committe
from django.contrib.auth.decorators import  login_required
from .decorators import unauthenticated_user
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Register API
@unauthenticated_user
def signUp(request):
    form = signUpForm
    if request.method == 'POST':
        form = signUpForm (request.POST)
        user = form.data.get ('username')
        print(user)
        SingnUpuser = User.objects.get(username=user)
        print(user)
        print(SingnUpuser)
        Role = SingnUpuser.user_role
        print(Role)
        if form.is_valid():
            if SingnUpuser is not None:
                if (SingnUpuser.registered == True):
                    user = form.save()
                    if (Role == "Voter"):
                        vtr = Voter(username=user)
                        vtr.save()
                        group = Group.objects.get(name='Voter')
                        user.groups.add(group)
                    elif (Role == "Candidate"):
                        vtr = candidate(username=user)
                        vtr.save()
                        group = Group.objects.get(name='Candidate')
                        user.groups.add(group)
                    elif (Role == "Committee"):
                        vtr = Election_Committe(username=user)
                        vtr1 = Voter(username=user)
                        vtr.save()
                        vtr1.save()
                        group = Group.objects.get(name='Committee')
                        user.groups.add(group)
                        group = Group.objects.get(name='Voter')
                        user.groups.add(group)
                    else:
                        group = Group.objects.get(name='Admin')
                        user.groups.add(group)
                    messages.success(request, 'Account created to ' + user)
                    return redirect('Loginpage')
                else:
                    messages.error(request, "Your Registration is not Approved yet please waite until Approve ")
            else:
                messages.error(request, "you are not Registered, Please Register first ")
        # try:
        #
        # except Exception as e:
        messages.error (request, "you are not Registered Yet, Please Register first ")
    context = {'form': form}
    return render (request, "account/signUp_Form.html", context)



@unauthenticated_user
def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate (username=username, password=password)
        if user is not None:
            login (request, user)
            return redirect ('showUser')
        else:
            messages.info (request, "username or password in incorrect")
            return render (request, "account/login_Form.html")
    context = {}
    return render (request, "account/login_Form.html", context)


@login_required(login_url='Loginpage')
def logoutpage(request):
    logout(request)
    return redirect('Loginpage')

@login_required(login_url='Loginpage')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/changePassword.html', {
        'form': form
    })



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            SingnUpuser = User.objects.get (username=request.data.get ('username'))
            Role = SingnUpuser.user_role
            if SingnUpuser is not None:
                if (SingnUpuser.registered == True):
                    user = serializer.save ()
                    if (Role == "Voter"):
                        vtr = Voter (username=user)
                        vtr.save ()
                        group = Group.objects.get (name='Voter')
                        user.groups.add (group)
                    elif (Role == "Candidate"):
                        vtr = candidate (username=user)
                        vtr.save ()
                        group = Group.objects.get (name='Candidate')
                        user.groups.add (group)
                    elif (Role == "Committee"):
                        vtr = Election_Committe (username=user)
                        vtr1 = Voter (username=user)
                        vtr.save ()
                        vtr1.save ()
                        group = Group.objects.get (name='Committee')
                        user.groups.add (group)
                        group = Group.objects.get (name='Voter')
                        user.groups.add (group)
                    else:
                        group = Group.objects.get (name='Admin')
                        user.groups.add (group)
                    return Response ({
                        "user": UserSerializer (user, context=self.get_serializer_context ()).data,
                        "token": AuthToken.objects.create (user)[1]
                    })
                return Response ("your registration is not approved yet")
            return Response ("you are not registration yet")
        except Exception as e:
            return Response(e)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny),
    def post(self, request, format=None):
        serializer = AuthTokenSerializer (data=request.data)
       # print (request.data)
        serializer.is_valid (raise_exception=True)
        user = serializer.validated_data['user']
        login (request, user)
        return super (LoginAPI, self).post (request, format=None)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)