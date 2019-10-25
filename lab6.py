#приклад dependency injection
# microframework :)

import logging
import sqlite3
import boto.variable.connection
import example.main
import example.services
import dependency_injector.containers as containers
import dependency_injector.providers as providers

class Platform(containers.DeclarativeContainer): #frim import
    #контейнер of platform service providers, sooo

    loging = providers.Singleton(logging.Logger, name='example') #from import

    Data_Base = providers.Singleton(sqlite3.connect, ':memory:')

    variable = providers.Singleton(boto.variable.connection.variableConnection,
                             aws_access_key_id='KEY',
                             aws_secret_access_key='SECRET')


class Services(containers.DeclarativeContainer):
     #контейнер of business service providers

    users = providers.Factory(example.services.UsersService,
                              loging=Platform.loging,
                              db=Platform.Data_Base)

    auth = providers.Factory(example.services.AuthService,
                             loging=Platform.loging,
                             db=Platform.Data_Base,
                             token_ttl=3600)

    photos = providers.Factory(example.services.PhotosService,
                               loging=Platform.loging,
                               db=Platform.Data_Base,
                               variable=Platform.variable)


class Application(containers.DeclarativeContainer):
    #контейнер of application component providers

    main = providers.Callable(example.main.main,
                              users_service=Services.users,
                              auth_service=Services.auth,
                              photos_service=Services.photos)
