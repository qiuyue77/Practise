### VIM配置

#### 1. 在.vimrc 中的配置
```
 i 写入模式、i插入之前、a插入之后、A行尾插入、I行首插入、o下行插入、O上行插入
x 删除光标后一个字符
d + ←→删除光标←→字符（d +3←）、dd删除一行（其实是剪切，p粘贴）
y+ ←→复制光标←→字符 （y+3←）
c 删除并进入写入模式
w 光标向下移动一个词
cw删除一个词并进入写入模式
b光标到上一个词
ciw词中删除一个词并进入写入模式
f 找词
/ 搜索、n下 N上
【y i c d f 】
esc 回到正常模式
:w保存
:q退出vim
:source $MYVIMRC 刷新vim
jkhl上下左右
:split 上下分屏 、:vsplit 左右分屏 Q退出

ctrl+o 返回光标刚才的位置
gf 打开光标所在文件

块模式
:normal A***     块指定的每行后面增加***
:normal K***     块指定的每行前面增加***


~/.vim/vimrc
noremap a b a键改b键
map a b a键改b键
syntax on 打开高亮
set number 显示行号
set wildmenu :命令补全
set hlsearch /搜索高亮
set incsearch 一面输入一面高亮
set ignorecase 忽略大小写43:35美化！ 

" ====================
" === Editor Setup ===
" ====================

" ===
" === System
" ===
set nocompatible
filetype on
filetype indent on
filetype plugin on
filetype plugin indent on
set mouse=a 可以使用鼠标
set encoding=utf-8

set clipboard=unnamed

" Prevent incorrect backgroung rendering
let &t_ut=''

" ===
" === Main code display
" ===
set number
set relativenumber
set ruler
set cursorline
syntax enable
syntax on

" ===
" === Editor behavior
" ===
" Better tab
tab键补全空格数
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
每行后面有空格就会显示出来
set list
set listchars=tab:▸\ ,trail:▫
set scrolloff=5

" Prevent auto line split
set wrap
set tw=0

set indentexpr=
" Better backspace 退格键可退回到上一行
set backspace=indent,eol,tart

set foldmethod=indent
set foldlevel=99

" Resize splits with arrow keys
map <up> :res +5<CR>
map <down> :res -5<CR>
map <left> :vertical resize-5<CR>
map <right> :vertical resize+5<CR>


vim中正常模式和编辑模式光标变化
let &t_SI = "\<Esc>]50;CursorShape=1\x7"
let &t_SR = "\<Esc>]50;CursorShape=2\x7"
let &t_EI = "\<Esc>]50;CursorShape=0\x7"

" ===
" === Restore Cursor Position
" ===  打开文件，光标会回到之前编辑位置
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
```


