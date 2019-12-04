## 配置



## 疑难

#### 1.解决中文乱码问题

编辑 /etc/gitconfig，末尾增加以下内容

```bash
[gui]  
    encoding = utf-8  
    # 代码库统一使用utf-8  
[i18n]  
    commitencoding = utf-8  
    # log编码  
[svn]  
    pathnameencoding = utf-8  
    # 支持中文路径  
[core]
    quotepath = false 
    # status引用路径不再是八进制（反过来说就是允许显示中文了）
```

编辑/etc/git-completion.bash，末尾增加以下内容

```bash
# 让ls命令能够正常显示中文
alias ls='ls --show-control-chars --color=auto' 
```

编辑/etc/inputrc，修改output-meta 和 convert-meta 属性值

```bash
set output-meta on # bash可以正常输入中文
set convert-meta off
```

编辑profile文件，末尾增加以下内容

```bash
export LESSHARESET=utf-8
```

