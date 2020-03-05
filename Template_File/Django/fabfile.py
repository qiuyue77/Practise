from fabric.api import (
    local,
    cd,
    run,
    execute,
    env,
)

env.user = 'data'

DOCKER = True

WEB = 'web'


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


def update():
    """
    update submodule dependencies.
    """
    local('git submodule init')
    local('git submodule update')


def runserver(port=8000):
    """
    Run Django development server.
    """
    cmd = 'python manage.py runserver 0.0.0.0:{}'.format(port)
    if DOCKER:
        local(
            'docker-compose run --rm -p {port}:{port} --name toutiao_web_run web {cmd}'
            .format(port=port, cmd=cmd))


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
        cmd = 'migrate toutiao {}'.format(version)
    manage(cmd)


def shell():
    """
    Open Django shell.
    """
    manage('shell')


def bash():
    """Execute bash in the `web` service."""
    _('bash')


def start_app(name):
    """
    Create Django application.  """
    _('python manage.py startapp {}'.format(name))


def clean():
    """
    Clean all .pyc files.
    """
    local("find . -name '*.pyc' '*.pyo' -type f -print -exec rm -rf {} \;")


def test():
    """Run Django unit tests.
    """
    manage('test')


def install():
    """pip install new dependencies
    """
    _("pip install -r requirements/base.txt")


def create_db(db='myblog'):
    '''
    create db if db not exists
    '''
    local('docker exec -it {db_container} mysql -uroot -proot -e '
          '"CREATE DATABASE IF NOT EXISTS {db};"'.format(
              db=db, db_container=config.db_container))


def drop_db(db='myblog'):
    '''
    drop db
    '''
    local('docker exec -it {db_container} mysql -uroot -proot -e '
          '"DROP DATABASE {db};"'.format(db=db,
                                         db_container=config.db_container))


def server_pull_update(branch='master'):
    with cd('/data/deploy_app/toutiao'):
        run('docker-compose pull web')
        run('git stash')
        run('git clean -fd')
        run('git checkout %s' % branch)
        run('git fetch origin %s' % branch)
        run('git reset --hard origin/%s' % branch)
        run('git pull --rebase origin %s:%s' % (branch, branch))


def server_db_migrate(container='prod'):
    with cd('/data/deploy_app/toutiao'):
        run('docker-compose pull web')
        run('docker-compose run --rm %s python manage.py migrate --noinput' %
            container)
        run('docker-compose run --rm %s python manage.py collectstatic --noinput'
            % container)


def server_service_restart(container='prod'):
    with cd('/data/deploy_app/toutiao'):
        run('docker-compose stop %s' % container)
        run('docker-compose rm -f %s' % container)
        run('docker-compose up -d %s' % container)


def deploy_test_from_local():
    """
    从本地发布测试
    :return:
    """
    clean()
    execute(server_db_migrate, 'web')
    execute(server_service_restart, 'web')
    execute(server_service_restart, 'test_celery')
    execute(server_service_restart, 'test_api')

