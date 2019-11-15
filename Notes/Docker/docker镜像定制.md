### 下载镜像

在docker hub上下载docker镜像，以ubuntu:18.04为基础，创建python环境

```bash
docker pull ubuntu:18.04
```

查看本地镜像

```bash
docker images
```

### 安装常用工具和Python

启动容器，并在容器内运行bash

```bash
docker run -it ubuntu:18.04 bash
```

由于原生ubuntu没有vim，所以需要先安装vim

```bash
apt update
apt install -y $buildDeps
apt install vim
```

更改官方源为清华源,先备份source.list,在修改

```bash
cp /etc/apt/sources.list /etc/apt/sources.list.backup
vim /etc/apt/sources.list
```

```
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
```

**如果报错："Certificate verification failed: The certificate is NOT trusted."**

```
sudo apt install ca-certificates
```

安装ping,wget,ifconfig等工具

```bash
apt install iputils-ping wget net-tools
```

安装Python3.7

```bash
apt install python3.7
ln -s /usr/bin/python3.7 /usr/bin/python
```

安装pip

```bash
apt install python3-pip
```

```bash
rm -rf /var/lib/apt/lists/*
apt purge -y --auto-remove $buildDeps
```

#### 配置Vim

```bash
vim ~/.vimrc
```

```
set ru
syntax on
set background=dark
set sw=4
set ts=4
set tabstop=4
set shiftwidth=4
set expandtab
filetype plugin on
set autoindent
set smartindent
set number
set viminfo='10,\"100,:20,%,n~/.viminfo
function! ResCur()
    if line("'\"") <= line("$")
        normal! g`"
        return 1
    endif
endfunction

augroup resCur
    autocmd!
    autocmd BufWinEnter * call ResCur()
augroup END

highlight WhiteSpaces ctermbg=green guibg=#55aa55
match WhiteSpaces /\s\+$/
```



### 提交镜像

查看刚配置好的容器，获取容器id [container id]

```bash
docker ps -a
```

提交更改，将容器打包成一个新的镜像

```bash
# docker commit [container id] [username]/[repository]:[tag]
docker commit [container id] qiuyue77/python3.7:latest
```

在查看本地的镜像

```bash
docker images
```

将新创建的镜像放到自己的docker hub上

```bash
# docker push [username]/[repository]:[tag]
docker push qiuyue77/python3.7:latest
```





#### 如果不能删除镜像，可能是有子镜像，需要先

```bash
docker image inspect --format='{{.RepoTags}} {{.Id}} {{.Parent}}' $(docker image ls -q --filter since=XXX) # XXX指镜像ID
```

根据父镜像再来删除镜像