from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from exam_app.webcam_socket import WebcamConsumer

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(
            [path('ws/video', WebcamConsumer.as_asgi())]
        ),
    }
)
