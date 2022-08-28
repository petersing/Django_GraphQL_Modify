# Django GraphQL Modify

## Important

This package is inspired by graphene-django. Since graphene-django has decided to terminate the update. I made this package in order to get graphene functionality to work in django 4.0 or higher. This package may still have many bugs, and I don't recommend using this package as a production use.

## Features

This package only retains the GraphQLView and DjangoObjectType functions, which are used very similarly to Graphene-Django.

### Settings

```python
GRAPHENE = {
    'SCHEMA': 'app.schema.schema'
}
```
### Urls

Similar to the original package, but graphiql functionality has been removed.

```python
from django.urls import path
from Django_GraphQL_Modify import GraphQLView

urlpatterns = [
    path('graphql/', GraphQLView.as_view()),
]
```

## Examples

Here is a simple Django model:

```python
from django.db import models

class TestModel(models.Model):
    email = models.CharField(max_length=100)
```

To create a GraphQL schema for it you simply have to write the following:

```python
from Django_GraphQL_Modify import DjangoObjectType
import graphene

class Test(DjangoObjectType):
    class Meta:
        model = TestModel

class Query(graphene.ObjectType):
    Tests = graphene.List(Test)

    def resolve_Tests(self, info):
        return TestModel.objects.all()

schema = graphene.Schema(query=Query)
```

Then you can query the schema:

```python
query = '''
    query {
      Tests {
        email,
      }
    }
'''
result = schema.execute(query)
```


## Original Plugins

| Plugin | README |
| ------ | ------ |
| graphene-django | [plugins/graphene-django/README.md][PlDb] |


   [PlDb]: <https://github.com/graphql-python/graphene-django/blob/main/README.md>
