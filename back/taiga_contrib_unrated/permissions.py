# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.conf import settings

from taiga.base.api.permissions import (TaigaResourcePermission, PermissionComponent)
from taiga.base import exceptions as exc
from . import services


class CanJoinProject(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        if not obj or not request.user.is_authenticated():
            return False

        if not services.can_user_join_project(request.user, obj):
            raise exc.PermissionDenied(_("You can't join the project if it is private, you're already a "
                                         "member, or there's no join role with slug '%s' (see "
                                         "UNRATED_PROJECT_JOIN_ROLE in config) you could join into"
                                         % settings.UNRATED_PROJECT_JOIN_ROLE))
        return True


class UnratedPermission(TaigaResourcePermission):
    join_project_perms = CanJoinProject()
