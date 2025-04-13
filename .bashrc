#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'


eval "$(starship init bash)"

PS1='[\u@\h \W]\$ '
fastfetch --colors-block-range-start 9 --colors-block-width 3 --title-format "Hello, {#31}{user-name}{#}"
. "$HOME/.cargo/env"
