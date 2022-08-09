from django.urls import path
from .views import Record, Login, Logout, FileUploadAPIView

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('upload/', FileUploadAPIView.as_view(), name="upload")
]
