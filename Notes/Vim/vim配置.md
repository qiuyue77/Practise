### VIM配置

#### 1. 在.vimrc 中的配置

 i 写入模式、i插入之前、a插入之后、A行尾插入、I行首插入、o下行插入、O上行插入
x 删除光标后一个字符
d + ←→删除光标←→字符（d +3←）、dd删除一行（其实是剪切，p粘贴）
y+ ←→复制光标←→字符 （y+3←）
c 删除并进入写入模式、w 光标向下移动一个词、cw删除一个词并进入写入模式、b光标到上一个词 、ciw词中删除一个词并进入写入模式，yi
f 找词
/ 搜索、n下 N上
【y i c d f 】
esc 回到正常模式
：w保存
：q退出vim
：source $MYVIMRC 刷新vim
jkhl上下左右
：split 上下分屏 、：vsplit 左右分屏 Q退出
~/.vim/vimrc
noremap a b a键改b键
map a b a键改b键
syntax on 打开高亮
set number 显示行号
set wildmenu ：命令补全
set hlsearch /搜索高亮
set incsearch 一面输入一面高亮
set ignorecase 忽略大小写43：35美化！ 

