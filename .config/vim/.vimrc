" __  ____   ____     _____ __  __ ____   ____ 
"|  \/  \ \ / /\ \   / /_ _|  \/  |  _ \ / ___|
"| |\/| |\ V /  \ \ / / | || |\/| | |_) | |    
"| |  | | | |    \ V /  | || |  | |  _ <| |___ 
"|_|  |_| |_|     \_/  |___|_|  |_|_| \_\\____|
                                              

" ===
" === Auto load for first time uses
" ===
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

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
set mouse=a
set encoding=utf-8

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
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set list
set listchars=tab:▸\ ,trail:▫
set scrolloff=5

" Prevent auto line aplit
set wrap
set tw=0

set indentexpr=
" Better backspace
set backspace=indent,eol,start

set foldmethod=indent
set foldlevel=99
" 光标在正常模式和编辑模式的不同显示
"-----terminal 1 ---------
"let &t_SI = "\<Esc>]50;CursorShape=1\x7"
"let &t_SR = "\<Esc>]50;CursorShape=2\x7"
"let &t_EI = "\<Esc>]50;CursorShape=0\x7"

"-----terminal 2 ---------
let &t_SI.="\e[5 q"
let &t_SR.="\e[3 q"
let &t_EI.="\e[1 q"
autocmd VimEnter * silent !echo -ne "\e[1 q"
autocmd VimLeave * silent !echo -ne "\e[5 q"

" ===
" === Status/command bar
" ===
set laststatus=2
set autochdir
set showcmd
set formatoptions-=tc

" Show command autocomplete
set wildignore=log/**,node_modules/**,target/**,tmp/**,*.rbc
set wildmenu
set wildmode=longest,list,full

" Searching options
set hlsearch
exec "nohlsearch"
set incsearch
set ignorecase
set smartcase

" ===
" === Restore Cursor Position
" ===
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" ===
" === Basic Mappings
" ===

" Set <LEADER> as <SPACE>
let mapleader=" "

" Column (:) mods
map ; :
map q; q:
map <LEADER>/ :!
map <LEADER>r :r !
map <LEADER>sr :%s/

" Search
noremap <LEADER><CR> :nohlsearch<CR>
noremap = nzz
noremap - Nzz

" Adjacent duplicate words
noremap <LEADER>fd /\(\<\w\+\>\)\_s*\1

"     ^
"     i
" < j   l >
"     k
"     v
noremap i k
noremap k j
noremap j h
noremap h i
noremap H I
" I/E keys for 5 times u/e
noremap I 5k
noremap K 5j
" J keys: go to the start of the line 
noremap J 0
" L keys: go to the end of the line 
noremap L $
" Faster in-line navigation
noremap W 5w
noremap B 5b

" Ctrl + U or E will move up/down the view port without moving the cursor
noremap <C-I> 5<C-y>
noremap <C-K> 5<C-e>
inoremap <C-I> <Esc>5<C-y>a
inoremap <C-K> <Esc>5<C-e>a

imap fj <Esc>

map si :set nosplitbelow<CR>:split<CR>
map sk :set splitbelow<CR>:split<CR>
map sj :set nosplitright<CR>:vsplit<CR>
map sl :set splitright<CR>:vsplit<CR>

" Resize splits with arrow keys
map <up> :res +5<CR>
map <down> :res -5<CR>
map <left> :vertical resize-5<CR>
map <right> :vertical resize+5<CR>

" Place the two screens up and down
noremap sh <C-w>t<C-w>K
" Place the two screens side by side
noremap sv <C-w>t<C-w>H

" Rotate screens
noremap srh <C-w>b<C-w>K
noremap srv <C-w>b<C-w>H


" ===
" === Tab management
" ===
" Create a new tab with tu
map ti :tabe<CR>
" Move around tabs with tn and ti
map tj :-tabnext<CR>
map tl :+tabnext<CR>
" Move the tabs with tmn and tmi
map tmj :-tabmove<CR>
map tml :+tabmove<CR>


map <LEADER>i <C-w>k
map <LEADER>k <C-w>j
map <LEADER>j <C-w>h
map <LEADER>l <C-w>l

" Disabling the default s key
map s <nop>
" Save & Quit
map S :w<CR>
map Q :q<CR>

" Press space twice to jump to the next '<++>' and edit it
map <LEADER><LEADER> <Esc>/<++><CR>:nohlsearch<CR>c4l

" Spelling Check with <space>sc
map <LEADER>sc :set spell!<CR>
noremap <C-x> ea<C-x>s
inoremap <C-x> <Esc>ea<C-x>s

" Call figlet
map tx :r !figlet 

" Compile function
map r :call CompileRunGcc()<CR>
func! CompileRunGcc()
  exec "w"
  if &filetype == 'java'
    exec "!javac %"
    exec "!time java %<"
  elseif &filetype == 'sh'
    :!time bash %
  elseif &filetype == 'python'
    silent! exec "!clear"
    exec "!time python3 %"
  elseif &filetype == 'html'
    exec "!firefox % &"
  elseif &filetype == 'markdown'
    exec "MarkdownPreview"
  elseif &filetype == 'vimwiki'
    exec "MarkdownPreview"
  endif
endfunc

" map R :source $MYVIMRC<CR>

map R :call CompileBuildrrr()<CR>
func! CompileBuildrrr()
  exec "w"
  if &filetype == 'vim'
    exec "source $MYVIMRC"
  elseif &filetype == 'markdown'
    exec "echo"
  endif
endfunc

call plug#begin('~/.vim/plugged')
" Pretty Dress
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'connorholyday/vim-snazzy'
"Plug 'NLKNguyen/papercolor-theme'
"Plug 'ayu-theme/ayu-vim'
"Plug 'bling/vim-bufferline'

" File navigation
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'ctrlpvim/ctrlp.vim', { 'on': 'CtrlP' }

" Taglist
Plug 'majutsushi/tagbar', { 'on': 'TagbarOpenAutoClose' }

" Error checking
Plug 'w0rp/ale'

" Auto Complete
" Plug 'Valloric/YouCompleteMe'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" Plug 'davidhalter/jedi-vim'

" Undo Tree
Plug 'mbbill/undotree/'

" Snippits
" Plug 'SirVer/ultisnips'  , { 'for': ['vim-plug', 'python'] }  
" Plug 'honza/vim-snippets', { 'for': ['vim-plug', 'python'] }

" Other visual enhancement
"Plug 'nathanaelkane/vim-indent-guides'
"Plug 'itchyny/vim-cursorword'
"Plug 'tmhedberg/SimpylFold'

" Git
"Plug 'rhysd/conflict-marker.vim'
Plug 'tpope/vim-fugitive'
"Plug 'mhinz/vim-signify'
Plug 'gisphm/vim-gitignore', { 'for': ['gitignore', 'vim-plug'] }

" HTML, CSS, JavaScript, PHP, JSON, etc.
"Plug 'elzr/vim-json'
"Plug 'hail2u/vim-css3-syntax'
"Plug 'spf13/PIV', { 'for' :['php', 'vim-plug'] }
"Plug 'gko/vim-coloresque', { 'for': ['vim-plug', 'php', 'html', 'javascript', 'css', 'less'] }
"Plug 'pangloss/vim-javascript', { 'for' :['javascript', 'vim-plug'] }
"Plug 'mattn/emmet-vim'

" Python
Plug 'vim-scripts/indentpython.vim'
" Plug 'vim-python/python-syntax', { 'for' :['python', 'vim-plug'] }

" Markdown
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install_sync() }, 'for' :['markdown', 'vim-plug'] }
Plug 'dhruvasagar/vim-table-mode', { 'on': 'TableModeToggle' }
"Plug 'vimwiki/vimwiki'

" For general writing
"Plug 'reedes/vim-wordy'
"Plug 'ron89/thesaurus_query.vim'

" Bookmarks
"Plug 'kshenoy/vim-signature'

" Other useful utilities
"Plug 'jiangmiao/auto-pairs'
"Plug 'terryma/vim-multiple-cursors'
"Plug 'junegunn/goyo.vim' " distraction free writing mode
"Plug 'ntpeters/vim-better-whitespace', { 'on': ['EnableWhitespace', 'ToggleWhitespace'] } "displays trailing whitespace (after :EnableWhitespace, vim slows down)
Plug 'tpope/vim-surround' " type ysks' to wrap the word with '' or type cs'` to change 'word' to `word`
"Plug 'godlygeek/tabular' " type ;Tabularize /= to align the =
"Plug 'gcmt/wildfire.vim' " in Visual mode, type i' to select all text in '', or type i) i] i} ip
"Plug 'scrooloose/nerdcommenter' " in <space>cc to comment a line

" Dependencies
"Plug 'MarcWeber/vim-addon-mw-utils'
"Plug 'kana/vim-textobj-user'
"Plug 'fadein/vim-FIGlet'

call plug#end()

" ===
" === Create a _machine_specific.vim file to adjust machine specific stuff, like python interpreter location
" ===
let has_machine_specific_file = 1
if empty(glob('~/.vim/_machine_specific.vim'))
  let has_machine_specific_file = 0
  exec "!cp ~/.vim/default_configs/_machine_specific_default.vim ~/.vim/_machine_specific.vim"
endif
source ~/.vim/_machine_specific.vim

"let g:SnazzyTransparent = 1
color snazzy

" ===
" === NERDTree
" ===
map tt :NERDTreeToggle<CR>
let NERDTreeMapOpenExpl = ""
let NERDTreeMapUpdir = ""
let NERDTreeMapUpdirKeepOpen = "l"
let NERDTreeMapOpenSplit = ""
let NERDTreeOpenVSplit = ""
let NERDTreeMapActivateNode = "i"
let NERDTreeMapOpenInTab = "o"
let NERDTreeMapPreview = ""
let NERDTreeMapCloseDir = "n"
let NERDTreeMapChangeRoot = "y"
let NERDTreeShowLineNumber = 1
let NERDTreeAutoCenter= 1
let NERDTreeShowHidden = 1
let NERDTreeIgnore = ['\.pyc','\~$','\.swp']
"打开vim时如果没有文件自动打开NERDTree
autocmd vimenter * if !argc()|NERDTree|endif
""当NERDTree为剩下的唯一窗口时自动关闭
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"设置树的显示图标
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'


"" ==
"" == NERDTree-git
"" ==
let g:NERDTreIndicatorMapCustom = {
            \ "Modified"   : "✹",
            \ "Staged"     : "✚",
            \ "Untracked"  : "✭",
            \ "Renamed"    : "➜",
            \ "Unmerged"   : "═",
            \ "Deleted"    : "✖",
            \ "Dirty"      : "✗",
            \ "Clean"      : "✔︎",
            \ "Unknown"    : "?"
            \ }

" " ===
" " === coc
" " ===
" " fix the most annoying bug that coc has
" silent! au BufEnter,BufRead,BufNewFile * silent! unmap if
" let g:coc_global_extensions = ['coc-python', 'coc-vimlsp', 'coc-html',
" 'coc-json', 'coc-css', 'coc-tsserver', 'coc-yank', 'coc-lists',
" 'coc-gitignore', 'coc-vimlsp', 'coc-tailwindcss', 'coc-stylelint']
" set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}
" " use <tab> for trigger completion and navigate to the next complete item
" function! s:check_back_space() abort
"   let col = col('.') - 1
"       return !col || getline('.')[col - 1]    =~ '\s'
"       endfunction
"       inoremap <silent><expr> <Tab>
"                   \ pumvisible() ? "\<C-n>" :
"                               \ <SID>check_back_space() ? "\<Tab>" :
"                                           \ coc#refresh()
"                                           inoremap <expr> <S-Tab>
"                                           pumvisible() ? "\<C-p>" :
"                                           "\<S-Tab>"
"                                           inoremap <silent><expr> <c-space>
"                                           coc#refresh()
"                                           " Useful commands
"                                           nnoremap <silent> <space>y
"                                           :<C-u>CocList -A --normal yank<cr>
"                                           nmap <silent> gd
"                                           <Plug>(coc-definition)
"                                           nmap <silent> gy
"                                           <Plug>(coc-type-definition)
"                                           nmap <silent> gi
"                                           <Plug>(coc-implementation)
"                                           nmap <silent> gr
"                                           <Plug>(coc-references)
"                                           nmap <leader>rn <Plug>(coc-rename)

" ===
" === ale
" ===
let b:ale_linters = ['pylint']
let b:ale_fixers = ['flake8']

" ===
" === You Complete ME
" ===
nnoremap gd :YcmCompleter GoToDefinitionElseDeclaration<CR>
nnoremap g/ :YcmCompleter GetDoc<CR>
nnoremap gt :YcmCompleter GetType<CR>
nnoremap gr :YcmCompleter GoToReferences<CR>
let g:ycm_autoclose_preview_window_after_completion=0
let g:ycm_autoclose_preview_window_after_insertion=1
let g:ycm_use_clangd = 0
"let g:ycm_python_binary_path = g:ycm_python_interpreter_path
let g:ycm_python_interpreter_path = system('which python3')
let g:ycm_python_binary_path = system('which python3')
"let g:ycm_key_list_select_completion   = ['<C-j>', '<C-n>', '<Down>']
"let g:ycm_key_list_previous_completion = ['<C-k>', '<C-p>', '<Up>']

" ===
" === Markdown
" ===
source ~/.vim/snippits.vim
"autocmd Filetype markdown map <leader>w yiWi[<esc>Ea](<esc>pa)
"autocmd Filetype markdown inoremap ,f <Esc>/<++><CR>:nohlsearch<CR>c4l
"autocmd Filetype markdown inoremap ,w <Esc>/ <++><CR>:nohlsearch<CR>c5l<CR>
"autocmd Filetype markdown inoremap ,n ---<Enter><Enter>
"autocmd Filetype markdown inoremap ,b **** <++><Esc>F*hi
"autocmd Filetype markdown inoremap ,s ~~~~ <++><Esc>F~hi
"autocmd Filetype markdown inoremap ,i ** <++><Esc>F*i
"autocmd Filetype markdown inoremap ,d `` <++><Esc>F`i
"autocmd Filetype markdown inoremap ,c ```<Enter><++><Enter>```<Enter><Enter><++><Esc>4kA
"autocmd Filetype markdown inoremap ,h ====<Space><++><Esc>F=hi
"autocmd Filetype markdown inoremap ,m - [ ] <Enter><++><ESC>kA
"autocmd Filetype markdown inoremap ,p ![](<++>) <++><Esc>F[a
"autocmd Filetype markdown inoremap ,a [](<++>) <++><Esc>F[a
"autocmd Filetype markdown inoremap ,1 #<Space><Enter><++><Esc>kA
"autocmd Filetype markdown inoremap ,2 ##<Space><Enter><++><Esc>kA
"autocmd Filetype markdown inoremap ,3 ###<Space><Enter><++><Esc>kA
"autocmd Filetype markdown inoremap ,4 ####<Space><Enter><++><Esc>kA
"autocmd Filetype markdown inoremap ,l --------<Enter>

" ===
" === MarkdownPreview
" ===
" let g:mkdp_auto_start = 0
" let g:mkdp_auto_close = 1
" let g:mkdp_refresh_slow = 0
" let g:mkdp_command_for_global = 0
" let g:mkdp_open_to_the_world = 0
" let g:mkdp_open_ip = ''
" let g:mkdp_browser = 'chromium'
" let g:mkdp_echo_preview_url = 0
" let g:mkdp_browserfunc = ''
" let g:mkdp_preview_options = {
"     \ 'mkit': {},
"     \ 'katex': {},
"     \ 'uml': {},
"     \ 'maid': {},
"     \ 'disable_sync_scroll': 0,
"     \ 'sync_scroll_type': 'middle',
"     \ 'hide_yaml_meta': 1
"     \ }
" let g:mkdp_markdown_css = ''
" let g:mkdp_highlight_css = ''
" let g:mkdp_port = ''
" let g:mkdp_page_title = '「${name}」'

" ===
" === vim-table-mode
" ===
map <LEADER>tm :TableModeToggle<CR>

" ===
" === CtrlP
" ===
map <C-p> :CtrlP<CR>
let g:ctrlp_prompt_mappings = {
  \ 'PrtSelectMove("j")':   ['<c-k>', '<down>'],
  \ 'PrtSelectMove("k")':   ['<c-i>', '<up>'],
  \ }
" 设置搜索时忽略的文件
let g:ctrlp_custom_ignore = {
    \ 'dir':  '\v[\/]\.(git|hg|svn|rvm)$',
    \ 'file': '\v\.(exe|so|dll|zip|tar|tar.gz|pyc)$',
    \ }
"默认使用全路径搜索，置1后按文件名搜索，准确率会有所提高，可以用<C-d>进行切换
let g:ctrlp_by_filename = 1


