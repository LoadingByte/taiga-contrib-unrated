# -*- coding: utf-8 -*-

from django.conf import settings
from taiga.projects import models


def add_user_to_project(user, project):
    join_role = project.get_roles().get(project=project, slug=settings.UNRATED_PROJECT_JOIN_ROLE)
    models.Membership.objects.create(user=user, project=project, role=join_role)


def can_user_join_project(user, project):
    is_member = project.memberships.filter(user=user).exists()
    join_role_exists = project.get_roles().filter(project=project, slug=settings.UNRATED_PROJECT_JOIN_ROLE).exists()
    return (not project.is_private) and (not is_member) and join_role_exists
