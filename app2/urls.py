from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskView

router=DefaultRouter()
router.register('tasks',TaskView)


urlpatterns=[
    path('',views.landingPageView,name="landingPage"),
    # path('pricingPage', views.pricingPageView, name="pricingPage"),
    path('contactPage',views.contactPageView, name="contactPage"),
    path('greetPage',views.greetPageView,name="greetPage"),
    path('pricing', views.pricingPageView2, name="pricingPage"),
    path('registerPage',views.registerPageView,name="registerPage"),
    # path('contactPage',views.contactPageView,name="contactPage")
    # path('aboutPage',views.aboutPageView,name="aboutPage")
    path('loginPage', views.loginView, name="loginPage"),
    path('dashboardPage', views.dashboardView, name='dashboardPage'),
    path('logOutPage',views.logOutView, name='logOutPage'),
    path('api/', include(router.urls)),
]