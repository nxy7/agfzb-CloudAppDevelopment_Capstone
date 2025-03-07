from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    path("about",view=views.about, name='about'),

    # path for contact us view
    path("contact",view=views.contact, name='contact'),

    # path for registration
    path("registration",view=views.registration, name='register'),
    path("registration_request",view=views.registration_request, name='register request'),

    # path for login
    path("login",view=views.login_request, name='login'),

    # path for logout
    path("logout",view=views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)