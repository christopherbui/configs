# Created by newuser for 5.9

# load prompt color
autoload -U colors && colors

# load autocompletion
autoload -Uz compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit

# load version control information
autoload -Uz vcs_info
precmd() { vcs_info }

# format vcs_info_msg_0_ variable for git status
zstyle ':vcs_info:*' enable git

zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' unstagedstr ' *'
zstyle ':vcs_info:*' stagedstr ' +'

zstyle ':vcs_info:git*+set-message:*' hooks git-untracked
zstyle ':vcs_info:git:*' formats '(%b%u%c)'
zstyle ':vcs_info:git:*' actionformats '(%b|%a%u%c)'

+vi-git-untracked(){
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == 'true' ]] && \
        git status --porcelain | grep '??' &> /dev/null ; then
        # This will show the marker if there are any untracked files in repo.
        # If instead you want to show the marker only if there are untracked
        # files in $PWD, use:
        #[[ -n $(git ls-files --others --exclude-standard) ]] ; then
        hook_com[staged]+=' ?'
    fi
}

# set up prompt
setopt prompt_subst
PROMPT='%{$fg_bold[red]%}[%{$fg_bold[yellow]%}%n%{$fg_bold[green]%}@%{$fg_bold[blue]%}%m %{$fg_bold[cyan]%}%1~%{$fg_bold[red]%}]%{$fg_bold[green]%}$%{$reset_color%} '
RPROMPT='%B%F{magenta}${vcs_info_msg_0_}%b%f'

# syntax highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# history
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000

# rust
export PATH="$HOME/.cargo/bin:$PATH"

# pfetch
export PF_INFO="ascii title os kernel pkgs de memory palette"
export PF_COL1=6
pfetch

# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv-virtualenv-init -)"

alias ls="lsd"
