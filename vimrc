set nocompatible              " be iMproved, required
set backspace=indent,eol,start
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'L9'
"Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'kchmck/vim-coffee-script'
"Plugin 'AutoComplPop'

Bundle 'Valloric/YouCompleteMe'
Bundle 'scrooloose/nerdtree'
Bundle 'Lokaltog/vim-powerline'
Bundle 'maksimr/vim-jsbeautify'
Bundle 'scrooloose/nerdcommenter'
"Bundle 'OmniCppComplete'  

syntax on


call vundle#end()            " required
filetype plugin indent on    " required

set nu
set mouse=a
set history=1000
set autoread
set so=20
set ruler
set ignorecase
set smartcase
"set ai
"set si
set ci
set wrap
set nocompatible

set encoding=utf-8
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set showmode

set clipboard=unnamed

"colorscheme desert
colorscheme brighton

set laststatus=2
let g:Powerline_colorscheme='solarized256'
set hlsearch

let mapleader=','

map j gj
map k gk

map <leader>n :NERDTreeToggle<CR>
map <leader>h :<leader>c<space>

" Smart way to move between windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

map <leader>tn :tabnew<cr>
map <leader>to :tabonly<cr>
map <leader>tc :tabclose<cr>
map <leader>tm :tabmove 
map <leader>t<leader> :tabnext 


map <Leader>v "gP
map <leader>c "+y

nmap <leader>0 $

map <C-i> gg=G

inoremap { {}<ESC>i

" swap iterm2 cursors in vim insert mode when using tmux
if exists('$TMUX')
    let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
    let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
else
    let &t_SI = "\<Esc>]50;CursorShape=1\x7"
    let &t_EI = "\<Esc>]50;CursorShape=0\x7"
endif
