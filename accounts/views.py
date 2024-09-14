# user_app/views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.validators import validate_email, FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from accounts.models import Profile
from datetime import datetime, date
from django.template.loader import render_to_string


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        return login_required(view, login_url='/login/')  # Specify your login URL here

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')  # Redirect to login page if user is not authenticated
        return super().dispatch(request, *args, **kwargs)

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'success': False})

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name, {'success': False})

    def post(self, request):
        success = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        date_of_birth_str = request.POST.get("date_of_birth")

        # Validate form data
        if not all([username, password, confirm_password, email, firstname, lastname, phone, date_of_birth_str]):
            messages.warning(request, 'Please fill in complete information')
        else:
            if len(username) < 5 or len(username) > 20:
                messages.warning(request, 'Username must be between 5 and 20 characters long')
            elif len(password) < 8 or len(password) > 20:
                messages.warning(request, 'Password must be between 8 and 20 characters long')
            else:
                try:
                    validate_email(email)

                    if password != confirm_password:
                        messages.warning(request, 'Password and Confirm Password do not match')
                    else:
                        if User.objects.filter(username=username).exists():
                            messages.warning(request, 'Username already registered')
                        elif User.objects.filter(email=email).exists():
                            messages.warning(request, 'Email already registered')
                        else:
                            try:
                                date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
                                if RegisterView.calculate_age(date_of_birth) < 18:
                                    messages.warning(request, 'You must be at least 18 years old to register')
                                else:
                                    user = User.objects.create_user(
                                        username=username,
                                        password=password,
                                        email=email,
                                        first_name=firstname,
                                        last_name=lastname
                                    )
                                    profile, created = Profile.objects.get_or_create(user=user)
                                    profile.phone_number = phone
                                    profile.date_of_birth = date_of_birth
                                    profile.save()

                                    self.send_registration_confirmation_email(request, email)

                                    messages.success(request, 'Created successfully')
                                    success = True
                            except ValueError:
                                messages.warning(request, 'Invalid date format')
                except ValidationError:
                    messages.warning(request, 'Invalid email address')

        return render(request, self.template_name, {'success': success})

    @staticmethod
    def calculate_age(birth_date):
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def send_registration_confirmation_email(self, request, email):
        subject = 'Registration Confirmation'
        message = render_to_string('email/email_template.html')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        html_message = render_to_string('email/email_template.html')

        try:
            send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=False)
            messages.success(request, 'Registration email sent successfully')
            return True
        except BadHeaderError:
            messages.error(request, 'Invalid header found in email')
            return False
        except Exception as e:
            messages.error(request, f'Failed to send registration email: {str(e)}')
            return False


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not all([username, password]):
            messages.warning(request, 'Please fill in complete information')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            try:
                user = User.objects.get(username=username)
                messages.warning(request, 'Incorrect password')
            except User.DoesNotExist:
                messages.warning(request, 'Account not found')

            return redirect('/login/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
