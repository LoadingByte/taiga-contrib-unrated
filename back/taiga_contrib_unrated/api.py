# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.conf import settings

from taiga.base.api import viewsets
from taiga.base.api.utils import get_object_or_404
from taiga.base.decorators import list_route
from taiga.base import exceptions as exc
from taiga.base import response

from taiga.projects.models import Project

from . import permissions
from . import services


class UnratedViewSet(viewsets.ViewSet):
    permission_classes = (permissions.UnratedPermission,)

    @list_route(methods=['GET'])
    def join_project(self, request, pk=None):
        project_slug = request.QUERY_PARAMS.get("project", None)
        project = get_object_or_404(Project, slug=project_slug)

        self.check_permissions(request, 'join_project', project)

        if not project.get_roles().filter(project=project, name=settings.UNRATED_PROJECT_JOIN_ROLE).exists():
            raise exc.NotFound(_("No join role with name '%s' in project '%s' (see UNRATED_PROJECT_JOIN_ROLE in config)"
                                   % (settings.UNRATED_PROJECT_JOIN_ROLE, project.slug)))
        if project.memberships.filter(user=user).exists():
            raise exc.IntegrityError(_("Already member of project '%s'" % project.slug))

        services.add_user_to_project(request.user, project)
        return response.Ok()
