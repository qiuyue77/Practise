# Manjaro 系统安装与配置
### 1.升级系统
#### 1.1修改更新源
```bash
# 对国内的镜像源进行测速及选择
sudo pacman-mirrors -i -c China -m rank
# 编辑pacman config
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

#### 1.2安装中文字体
```bash
sudo pacman -S wqy-bitmapfont wqy-microhei wqy-microhei-lite wqy-zenhei adobe-source-han-mono-cn-fonts adobe-source-han-sans-cn-fonts adobe-source-han-serif-cn-fonts
```

#### 1.3耳机声卡设置
```bash
sudo pacman -S pavucontrol
pavucontrol
```

### 2.安装app
#### 安装vim
```
# 自行复制.ssh
git clone git@qiuyue77/Practise/.config
cp -r Practise/.config/vim ~/.vim
sudo pacman -S vim
vim # 然后等待安装插件
```

#### 安装nodejs
```
# 由于vim插件coc需要nodejs，须先安装
sudo pacman -S nodejs npm
# 安装cnpm，使用其他镜像（例子为淘宝镜像）
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
# 前端脚手架工具
sudo cnpm isntall -g fis3
```

#### 更改pacman的状态
```
sudo -E vim /etc/pacman.conf
/Color
# 去掉Color前的备注
# 保存退出
sudo pacman -Syy # 刷新pacman
```

#### 更新shell 为 fish
```
sudo pacman -S fish
# 更新默认打开为fish
which fish
chsh -s /usr/bin/fish
# 安装oh-my fish
curl -L https://get.oh-my.fish | fish
# 或者 curl -L https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish

# 设置fish，选择主题等
fish_config
# 通过omf install安装插件
```
##### 通过alias来绑定快捷键
```
alias c clear # 快捷键c 清屏
funcsave c # 保存 快捷键c

alias l 'ls -la' # 快捷键l 显示隐藏文件及详细信息
funcsave l

alias sudo 'sudo -E'
funcsave sudo
# 刷新i3 config
```

#### 更新shell 为 zsh
```bash
sudo pacman -S zsh # manjaro应该自带zsh
# 查看已安装shells列表
cat /etc/shells
# 安装`oh-my-zsh`
# sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/ohmyzsh/ohmyzsh.git
sh ohmyzsh/tools/install.sh
# 更换shell
chsh -s /bin/zsh
chsh -s /usr/bin/zsh
```
复制粘贴自己的zshrc
```
cp ~/.config/zsh/zshrc ~/.zshrc
```
##### 安装自动跳转、语法建议、语法高亮插件
```
sudo pacman -S autojump
sudo git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

#### 安装i3 及相关设置
```
sudo pacman -S i3
reboot
```
##### 登录界面时，选择i3登录，进入系统后，选择默认添加config，并选择win键为super键
##### 刷新i3 的config设置默认快捷键为 win+shift+r
##### 尽量复制自己的设置
```
# 启动i3自动启动程序 exec_always 
# 启动i3自动关闭程序 exec_killall 
# --no-startup-id 当启动了某些并不支持启动提醒的某脚本或程序时，鼠标指针会逗留在忙碌状态六十秒以上。为防止此现象，凡是 exec 命令都均加 --no-startup-id
```

##### i3窗口与窗口之间设置空格
```
sudo pacman -S i3-gaps
# i3 config中最后添加
gaps inner 8
```

##### 删除i3窗口下的状态栏
```
sudo pacman -R i3status
```

##### 设置分辨率
```
vim ~/.Xresources
Xft.dpi: 200 # 显示器分辨率高的可选择200， 低的可选择不设置
# 保存退出
reboot
```

#### 安装alacrity 及设置   （更新terminal）
```
sudo pacman -S alacritty
# 编辑i3默认打开alacritty
vim ~/.config/i3/config
# 找到 start a terminal 修改为
bindsym $mod+Return exec alacritty
# 复制alacritty.yml到~/.config/alacritty
```

#### 安装dmenu 及设置  (i3的导航菜单栏)
```
sudo pacman -S dmemu
# i3中默认快捷键win+d 打开
```

#### 安装xorg及设置 （更改硬件设置，主要更改键位）
```
sudo pacman -S xorg
xmodmap -pke > ~/.xmodmap
vim ~/.xmodmap
# 新建窗口 win+enter
xev # 可查看键盘键位所代表的key值
# 尽量复制自己的文件
# 更新key值后，刷新xmodmap
xmodmap ~/.xmodmap
# i3 config 中添加自启动
exec_killall xmodmap
xmodmap ~/.xmodmap
```

#### 安装lxappearance及设置（主题）
```
sudo pacman -S lxappearance
lxappearance # 选择主题
```

#### 安装feh及设置（壁纸）
```
sudo pacman -S feh
# 安装feh管理器
sudo pacman -S variety
# win+s 输入 variety 设置壁纸等
```

#### 安装compton及设置（渲染器）
```
sudo pacman -S compton
# win+s 输入 compton 渲染
```

#### 安装输入法及设置
```
sudo pacman -S fcitx fcitx-im fcitx-configtool
sudo pacman -S fcitx-sogoupinyin
# 如果未安装成功，需添加yaourt来安装qtwebkit-bin
# sudo pacman -S yaourt
# sudo pacman -S base-devel
# yaourt -S qtwebkit-bin
# sudo pacman -S fcitx-sogoupinyin
vim ~/.xprofile
# 添加如下文本
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

#### 安装chrome开源版chromium
```
sudo pacman -S chromium
```

#### 安装vlc，视屏播放器
```
sudo pacman -S vlc
```

#### 安装virtualbox，虚拟机
```
sudo pacman -S virtualbox
```

#### 安装ranger，文件管理器
```
sudo pacman -S ranger
# 复制自己的ranger config
```

#### 安装polybar，屏幕上方显示状态栏
```
sudo pacman -S polybar
mkdir ~/.config/polybar && cp /usr/share/doc/polybar/config ~/.config/polybar/
# 默认打开方式来
polybar example
# 自启动的脚本设置
vim launch.sh
killall polybar
polybar example
# 保存，并更改为可自行文件
chmod +x launch.ch
vim ~/.config/i3/config
# 添加如下
exec_always ~/.config/polybar/launch.ch
# 刷新i3 config
```
#### 安装docker
```
sudo pacman -S docker
# 启动docker服务
sudo systemctl start docker
# 查看docker服务的状态
sudo systemctl status docker
# 设置docker开机启动服务
systemctl enable docker
```

#### 安装网易云音乐
```
sudo pacman -S netease-cloud-music
```

#### 安装微信！！！！（未成功）
```
sudo pacman -S aurman
aurman -S deepin-wechat
```

#### 安装Typora

```bash
sudo pacman -S typora
```


### 3.i3桌面优化

