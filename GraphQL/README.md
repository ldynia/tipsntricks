# Echo Query

```python
import graphene
from graphene import ObjectType


class Query(ObjectType):
    pass


class Mutation(ObjectType):
    pass


class EchoType(graphene.ObjectType):
    echo_msg = graphene.String()


class EchoQuery(graphene.ObjectType):
    echo = graphene.String(args={'msg': graphene.String(required=True)})
    echo_msg = graphene.Field(EchoType, msg=graphene.String(required=True))

    def resolve_echo(root, info, **kwargs):
        return kwargs['msg']

    def resolve_echo_msg(root, info, **kwargs):
        return {'echo_msg': kwargs['msg']}


class PingType(graphene.ObjectType):
    status_code = graphene.Int()
    status = graphene.String()


class PingQuery(graphene.ObjectType):

    ping = graphene.Field(PingType)

    def resolve_ping(root, info, **kwargs):
        return {
            'status_code': 200,
            'status': 'success'
        }


setattr(Query, "echo", EchoQuery.echo)
setattr(Query, "resolve_echo", EchoQuery.resolve_echo)

setattr(Query, "ping", PingQuery.ping)
setattr(Query, "resolve_ping", PingQuery.resolve_ping)

setattr(Query, "echo_msg", EchoQuery.echo_msg)
setattr(Query, "resolve_echo_msg", EchoQuery.resolve_echo_msg)



```

# Query

```
mutation MyMutation($users: [ID]) {
  __typename
  updateWorkspace(owner: "2", id: "4", users: $users) {
    workspace {
      id
      name
    }
  }
}

{"users": [1,2,3]}
```

```
mutation MyMutation($workspaceId: ID!, $usersId: [ID]!, $permission: permission!) {
  __typename
  createWorkspacePermission(workspaceId: $workspaceId, usersId: $usersId, permission: $permission) {
    ok
  }
}

{"workspaceId": 24, "usersId": [1,2], "permission": "READ"}
```


```python
import graphene
import graphene_django
import typing

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from graphql import GraphQLError
from guardian.shortcuts import get_perms

from general.PermissionUtility import PermissionUtility


if PermissionUtility.permissionsEnabled():

    PermitterModel = PermissionUtility.permissionModel()

    class ModelUserPermissionType(graphene_django.DjangoObjectType):
        """
        Type for permitter to show on dashboard.
        """

        class Meta:
            """
            The model and fields to expose.
            """
            model = User
            skip_registry = True
            fields = (
                "id",
                "email",
                "username",
                "first_name",
                "last_name",
            )

        owner = graphene.Boolean(default_value=False)
        permissions = graphene.List(graphene.String)

        def resolve_permissions(self, info):
            permitter = PermitterModel.objects.get(id=info.variable_values['permitterId'])
            return get_perms(self, permitter)

        def resolve_owner(self, info):
            permitter = PermitterModel.objects.get(id=info.variable_values['permitterId'])
            return permitter.owner == self


    class ModelUserPermissionQuery(graphene.ObjectType):
        """
        Query for getting permitter to show on the dashboard.
        """
        permitter_users = graphene.Field(
            graphene.List(ModelUserPermissionType),
            permitter_id=graphene.ID(required=True, description="Permitter id"),
            description="Query for getting users that belong to queried permitter."
        )

        @staticmethod
        def resolve_permitter_users(root: typing.Optional[QuerySet], info: graphene.ResolveInfo, permitter_id: graphene.ID, **kwargs) -> typing.List[User]:
            """
            Get users that should be shown on the dashboard.

            :param root: The root query.
            :param info: The query context.
            :param permitter_id: Permitter id.

            :return: The relevant users.
            """
            _ = (root)

            permitter = PermitterModel.objects.filter(id=permitter_id).first()
            if not permitter:
                raise GraphQLError(f"Permitter with id {permitter_id} doesn't exist.")

            # Obtain all users associated with permitter
            ids = list(permitter.users.values_list('id', flat=True)) + [permitter.owner.id]

            return User.objects.filter(id__in=ids)
```
