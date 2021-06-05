import coreapi
from rest_framework.filters import BaseFilterBackend


class UserProfileFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        params = ["user"]
        QueryParameters = []
        for param in params:
            QueryParameters.append(
                coreapi.Field(name=param, required=False, location="query")
            )
        return QueryParameters
