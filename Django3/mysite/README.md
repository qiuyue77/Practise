# Django-mysite 环境搭建及项目配置

### 前期准备

* Docker
* fabric 3 版本

### 配置所需服务的 docker 容器

#### 安装设置数据库

```bash
git clone https://github.com/qiuue77/database-docker-services
cd database-docker-services && mkdir -p data/mysql
# 编辑 `docker-compose.yml` 修改数据库 root 密码
docker-compose up -d
# 等待一会会
docker-compose exec mysql mysql -p  # 登录 mysql
# 输入数据库 root 密码
CREATE DATABASE mysite;
exit;
```

#### 配置项目

```bash
git clone git@xxxx.git
cd mysite
# 编辑 mysite/settings.py 修改数据库密码
fab -l # 查看 fab 操作
fab test # 运行测试
fab migrate # 迁移数据库
fab runserver # 运行 web 服务器
fab manage:createsuperuser # 创建超级用户
```

## 常用命令

```bash
fab -l
```

`Available commands`:

|----------------|------------------------------------|
| bash           | Execute bash in the `web` service. |
| clean          | Clean all .pyc files.              |
| sclean         | Clean all .pyc files by root.      |
| create_db      | create db if db not exists         |
| drop_db        | drop db                            |
| install        | pip install new dependencies       |
| makemigrations | Generate database migration files. |
| manage         | Run django manage command.         |
| migrate        | Database migration.                |
| runserver      | Run Django development server.     |
| shell          | Open Django shell.                 |
| start_app      | Create Django application.         |
| test           | Run Django unit tests.             |
