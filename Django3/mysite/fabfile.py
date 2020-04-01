# coding: utf-8

from fabric.api import local

#from fabric.api import (
#    cd,
#    run,
#    execute,
#    env,
#    settings,
#)

# TEST_ENV = '10.9.255.43'
# PROD_DB = '10.9.254.134'
# PRO_ENV_NODE1 = '10.9.250.68'

DOCKER = True
name = 'mysite1'


class Config(object):
    db_container = 'product_mysql'


config = Config()


def _(command):
    """
    Run command
    """
    if DOCKER:
        local('docker-compose run --rm web  {}'.format(command))
    else:
        local(command)


def runserver(port=7000):
    """
    Run Django development server.
    """
    cmd = 'python manage.py runserver 0.0.0.0:{}'.format(port)
    if DOCKER:
        local(
            f'docker-compose run --rm -p {port}:{port} --name {name}_web_run web {cmd}'
        )


def manage(cmd):
    """
    Run django manage command.
    """
    _('python manage.py {}'.format(cmd))


def makemigrations(merge=False):
    """
    Generate database migration files.
    """
    cmd = 'makemigrations --merge' if merge else 'makemigrations'
    manage(cmd)


def migrate(version=None):
    """
    Database migration.
    """
    if version is None:
        cmd = 'migrate'
    else:
        cmd = f'migrate {name} {version}'
    manage(cmd)


def shell():
    """
    Open Django shell.
    """
    manage('shell')


def bash():
    """Execute bash in the `web` service."""
    _('bash')


def start_app(app_name):
    """
    Create Django application.  """
    _(f'python manage.py startapp {app_name}')


def clean(cmd=""):
    """
    Clean all .pyc files.
    """
    curly_braces = '{} \\'
    local(
        f'{cmd} find . -name "*.pyc" -type f -print -exec rm -rf {curly_braces};'
    )


def sclean():
    """
    Clean all .pyc files by root.
    """
    clean('sudo')


def test():
    """
    Run Django unit tests.
    """
    manage('test')


def install():
    """
    pip install new dependencies
    """
    _("pip install -r requirements/base.txt")


def create_db(db=name):
    '''
    create db if db not exists
    '''
    local('docker exec -it {db_container} mysql -uroot -p -e '
          '"CREATE DATABASE IF NOT EXISTS {db};"'.format(
              db=db, db_container=config.db_container))


def drop_db(db=name):
    '''
    drop db
    '''
    local('docker exec -it {db_container} mysql -uroot -p -e '
          '"DROP DATABASE {db};"'.format(db=db,
                                         db_container=config.db_container))


# def server_pull_update(branch='master'):
#     with cd(f'/data/deploy_app/{name}'):
#         run('docker-compose pull web')
#         run('git stash')
#         run('git clean -fd')
#         run('git checkout %s' % branch)
#         run('git fetch origin %s' % branch)
#         run('git reset --hard origin/%s' % branch)
#         run('git pull --rebase origin %s:%s' % (branch, branch))

# def server_db_migrate(container='prod'):
#     with cd(f'/data/deploy_app/{name}'):
#         run('docker-compose pull web')
#         run('docker-compose run --rm %s python manage.py migrate --noinput' % container)
#         run('docker-compose run --rm %s python manage.py collectstatic --noinput' % container)

# def server_service_restart(container='prod'):
#     with cd(f'/data/deploy_app/{name}'):
#         run('docker-compose stop %s' % container)
#         run('docker-compose rm -f %s' % container)
#         run('docker-compose up -d %s' % container)

# def deploy_test_docker(branch='dev'):
#     '''
#     从gitlab 发布测试环境
#     '''
#     execute(server_pull_update, branch, hosts=[TEST_ENV])
#     execute(server_db_migrate, 'web', hosts=[TEST_ENV])
#     execute(server_service_restart, 'web', hosts=[TEST_ENV])
#     execute(server_service_restart, 'test_celery', hosts=[TEST_ENV])
#     execute(server_service_restart, 'test_api', hosts=[TEST_ENV])

# def deploy_pro_docker(branch='master'):
#     '''
#     从gitlab 发布生产环境
#     '''
#     execute(server_pull_update, branch, hosts=[PRO_ENV_NODE1])
#     execute(server_db_migrate, 'prod', hosts=[PRO_ENV_NODE1])
#     execute(server_service_restart, 'prod', hosts=[PRO_ENV_NODE1])
#     execute(server_service_restart, 'pro_celery', hosts=[PRO_ENV_NODE1])
#     execute(server_service_restart, 'pro_xiaocx_api', hosts=[PRO_ENV_NODE1])
