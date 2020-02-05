#### pacman 基本用法
| 命令                      | 说明                                        |
| --                        | --                                          |
| pacman -Sy                | #仅同步源                                   |
| pacman -Syy               | #强制仅同步源                               |
| pacman -Su                | #更新系统                                   |
| pacman -Syu               | #先同步源，并更新系统                       |
| pacman -Syyu              | #强制先同步源，并更新系统                   |
| pacman -Sc                | #清理/var/cache/pacman/pkg目录下的旧包      |
| pacman -Scc               | #清除所有下载的包和数据库                   |
| pacman -S   abc           | #从本地数据库中得到abc的信息，下载安装abc包 |
| pacman -Si abc            | #从数据库中搜索包abc的信息                  |
| pacman -Ss abc            | #搜索有关abc信息的包                        |
| pacman -Sy abc            | #和源同步后安装名为abc的包                  |
| pacman -Sf abc            | #强制安装包abc                              |
| pacman -R   abc           | #删除abc包                                  |
| pacman -Rd abc            | #强制删除被依赖的包                         |
| pacman -Rc abc            | #删除abc包和依赖abc的包                     |
| pacman -Rsc abc           | #删除abc包和abc依赖的包                     |
| pacman -Rns abc           | #删除abc包、abc依赖的包、全局配置文件       |
| pacman -Q                 | #列出已经安装的软件包及其版本号             |
| pacman -Qe                | #列出已经安装的软件包及其版本号(自己安装的) |
| pacman -Qq                | #列出已经安装的软件包（不含版本号）         |
| pacman -Qdt               | #列出没有依赖或者被依赖的包                 |
| pacman -R $(pacman -Qdtq) | #删除没有依赖或者被依赖的包                 |
| pacman -Q abc             | #检查 abc 软件包是否已经安装                |
| pacman -Qs abc            | #列出名字带有 abc 的软件包                  |
| pacman -Qi abc            | #列出已安装的包abc的详细信息                |
| pacman -Ql abc            | #列出abc软件包的所有文件                    |
| pacman -Qo /path/to/abc   | #列出abc文件所属的软件包                    |
| pacman -U   abc           | #安装网址或目录下的abc包，或新编译的abc包   |
| pacman -Sd abc            | #忽略依赖性问题，安装包abc                  |
| pacman -Su --ignore foo   | #升级时不升级包foo                          |
| pacman -Sg abc            | #查询abc这个包组包含的软件包                |
#### pacman 配置
配置文件在/etc/pacman.config

