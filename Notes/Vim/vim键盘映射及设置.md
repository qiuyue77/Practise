## 映射

### 不同模式下的键盘映射  

| Command  | Command2  | Normal | Visual | Operator Pending | Insert | Command Line |
| -------- | :-------- | :----: | :----: | :--------------: | :----: | :----------: |
| :map     | :noremap  |   Y    |   Y    |        Y         |        |              |
| :nmap    | :nnoremap |   Y    |        |                  |        |              |
| :vmap    | :vnoremap |        |   Y    |                  |        |              |
| :omap    | :onoremap |        |        |        Y         |        |              |
| :map!    | :noremap! |        |        |                  |   Y    |      Y       |
| :imap    | :inoremap |        |        |                  |   Y    |              |
| :cmap    | :cnoremap |        |        |                  |        |      Y       |
| :nnormal |           |   Y    |        |                  |        |              |
| :inormal |           |        |        |                  |   Y    |              |

### 取消不同模式下的键盘映射

| Command | Normal | Visual | Operator Pending | Insert | Command Line |
| :------ | :----: | :----: | :--------------: | :----: | :----------: |
| :unmap  |   Y    |   Y    |        Y         |        |              |
| :nunmap |   Y    |        |                  |        |              |
| :vunmap |        |   Y    |                  |        |              |
| :ounmap |        |        |        Y         |        |              |
| :unmap! |        |        |                  |   Y    |      Y       |
| :iunmap |        |        |                  |   Y    |              |
| :cunmap |        |        |                  |        |      Y       |

> 注： 必须为:unmap命令指定一个参数。如果未指定任何参数，那么系统将会报错，而不会取消所有的键盘映射。 
>
> ```shell
> :unmap <F10>
> ```

### 键盘所对应字符表达

| 代表字符          | 键位                  |
| ----------------- | --------------------- |
| <Esc>             | Escape 退出           |
| <CR>              | Enter 回车键          |
| <Tab>             | Table Tab键           |
| <>                |                       |
| <Space>           | Space 空格键          |
| <Up>              | cursor-up 光标上移    |
| <Down>            | cursor-down 光标下移  |
| <Left>            | cursor-left 光标左移  |
| <Right>           | cursor-right 光标右移 |
| <C-key>           | Ctrl-key              |
| <S-key>           | Shift-key             |
| <A-key> / <M-key> | Alt-key               |





## 配置

##### 自动补全

```shell
:inoremap ( ()<ESC>i
:inoremap ) <c-r>=ClosePair(')')<CR>
:inoremap { {<CR><CR>}<ESC>0ki<Tab>
:inoremap } <c-r>=ClosePair('}')<CR>
function ClosePair(char)
if getline('.')[col('.') - 1] == a:char
return "\<Right>"
else
return a:char
endif
endf
```

