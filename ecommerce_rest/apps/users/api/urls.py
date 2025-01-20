from django.url import path

urlpatterns = [
    path('usuario/',UserAPIView.as_view(), name = 'usuario_api')
]