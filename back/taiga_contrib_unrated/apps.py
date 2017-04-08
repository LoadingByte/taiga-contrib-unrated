# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf.urls import include, url


class TaigaContribUnratedAppConfig(AppConfig):
    name = "taiga_contrib_unrated"
    verbose_name = "Taiga contrib unrated App Config"

    def ready(self):
        from taiga.base import routers
        from taiga.urls import urlpatterns
        from .api import UnratedViewSet

        router = routers.DefaultRouter(trailing_slash=False)
        router.register(r"unrated", UnratedViewSet, base_name="unrated")
        urlpatterns.append(url(r'^api/v1/', include(router.urls)))
