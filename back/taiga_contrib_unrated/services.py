# -*- coding: utf-8 -*-

from django.conf import settings
from taiga.projects import models


def add_user_to_project(user, project):
    join_role = project.get_roles().get(project=project, slug=settings.UNRATED_PROJECT_JOIN_ROLE)
    models.Membership.objects.create(user=user, project=project, role=join_role)


def can_user_join_project(user, project):
    return not project.is_private
