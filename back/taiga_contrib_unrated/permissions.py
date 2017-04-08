# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from taiga.base.api.permissions import (TaigaResourcePermission, PermissionComponent)
from taiga.base import exceptions as exc
from . import services


class CanJoinProject(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        if not obj or not request.user.is_authenticated():
            return False

        if not services.can_user_join_project(request.user, obj):
            raise exc.PermissionDenied(_("Can't join project '%s' because it is private" % obj.slug))

        return True


class UnratedPermission(TaigaResourcePermission):
    join_project_perms = CanJoinProject()
