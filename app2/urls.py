from django.urls import path
from . import views
urlpatterns=[
    path('',views.landingPageView,name="landingPage"),
    path('pricingPage', views.pricingPageView, name="pricingPage"),
    path('contactPage',views.contactPageView, name="contactPage"),
    path('greetPage',views.greetPageView,name="greetPage"),
    path('pricingPage2', views.pricingPageView2, name="pricingPage"),
    path('registerPage',views.registerPageView,name="registerPage"),
    # path('contactPage',views.contactPageView,name="contactPage")
    # path('aboutPage',views.aboutPageView,name="aboutPage")
    path('loginPage', views.loginView, name="loginPage"),
    path('dashboardPage', views.dashboardView, name='dashboardPage')
]