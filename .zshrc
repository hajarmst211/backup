# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

### Zinit Installation
if [[ ! -f $HOME/.zinit/bin/zinit.zsh ]]; then
    print -P "%F{33}▓▒░ %F{160}Installing zinit...%f"
    command mkdir -p "$HOME/.zinit" && \
    command git clone https://github.com/zdharma-continuum/zinit "$HOME/.zinit/bin"
fi

source "$HOME/.zinit/bin/zinit.zsh"
autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

zinit light romkatv/powerlevel10k
zinit light zsh-users/zsh-autosuggestions
zinit light marlonrichert/zsh-autocomplete

alias r="source ~/.zshrc"
alias c='clear'
alias rc="clear && source ~/.zshrc"
alias instal="sudo pacman -S"
alias ls="exa -lh --time modified --no-permissions --no-user --icons --git"
alias cvenv="python -m venv .venv"
alias avenv="source .venv/bin/activate"
alias dvenv="deactivate"
alias rvenv="pip freeze > requirements.txt"
alias bl="blueman-manager"
alias wifi='nmtui'
alias sd="sudo shutdown now"
alias py="python"
alias fm="thunar &"
alias rb="sudo reboot now"

(cat ~/.cache/wal/sequences &)
bindkey '^I' autosuggest-accept

# Number of commands to keep in memory during a session
HISTSIZE=10000

# Number of commands to save in the history file
SAVEHIST=20000

# History file location
HISTFILE=~/.zsh_history

#make sure it's always in the end
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
