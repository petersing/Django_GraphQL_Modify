import setuptools

setuptools.setup(
    name = 'Django_GraphQL_Modify',
    version = '0.0.1',
    author = 'Peter Cheung',
    description= 'This package is inspired by graphene-django. Since graphene-django has decided to terminate the update. To get graphene functionality to work in django 4.0 or later, I made this package',
    packages= ['Django_GraphQL_Modify'],
    install_requires=['six', 'Django', 'graphene'],
)