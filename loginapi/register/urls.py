
from register import views
from django.urls import path, include
from .views import (
    loginapiListApiView,
)

urlpatterns = [

    path("users", views.ListUserAPIView.as_view()),
    path("create/", views.CreateUserAPIView.as_view()),
    path("update/<int:pk>/", views.UpdateUserAPIView.as_view()),
    path("delete/<int:pk>/", views.DeleteUserAPIView.as_view()),
    # path("register/", views.ListCarAPIView.as_view(), name="_list"),
    # path("regiser/create/", views.CreateCarAPIView.as_view(), name="car_create"),
    # path("register/update/<int:pk>/",
    #      views.UpdateCarAPIView.as_view(), name="car_update"),
    # path("register/delete/<int:pk>/",

    #      views.DeleteCarAPIView.as_view(), name="car_delete"),

]
