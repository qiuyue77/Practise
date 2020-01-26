# Manjaro 系统配置
### 升级系统
#### 修改更新源
```
sudo nano /etc/pacman.conf
# 找到[mutilib]相关配置的位置在下方
# 添加如下信息：
[archlinuxcn]
SigLevel = Never
Server = https://mirrois.tuna.tsinghua.edu.cn/archlinuxcn/$arch
# 保存后执行
# 更新同步源及导入GPG key
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
# 同步源并更新系统
sudo pacman -Syyu
```
#### 
<++>#### 
<++>#### 
<++>#### 
<++>
