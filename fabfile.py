from fabric.api import *


def reqs():
    ''' Freeezes requirements to a requirements/* directory'''
    packages = local('pip freeze', capture = True)
    with open('requirements/development.txt', 'w') as f:
        f.write(packages)


