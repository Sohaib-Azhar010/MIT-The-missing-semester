import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, but I am not stopping")

signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print("\r{}".format(i), end="")
    i += 1



# TOPICS :    1.JOB CONTROL           2.TERMINAL MULTIPLEXER         3.DOT FILES   4.REMOTE MACHINES
#     Sessions > Windows > Panes





#         1.JOB CONTROL

# CTRL + C , will interrupt the execution 
# CTRL + Z , will stop the process 
# CTRL + \ , will quit the program



# $ sleep 1000
# ^Z
# [1]  + 18653 suspended  sleep 1000

# $ nohup sleep 2000 &
# [2] 18745
# appending output to nohup.out

# $ jobs
# [1]  + suspended  sleep 1000
# [2]  - running    nohup sleep 2000

# $ bg %1
# [1]  - 18653 continued  sleep 1000

# $ jobs
# [1]  - running    sleep 1000
# [2]  + running    nohup sleep 2000

# $ kill -STOP %1
# [1]  + 18653 suspended (signal)  sleep 1000

# $ jobs
# [1]  + suspended (signal)  sleep 1000
# [2]  - running    nohup sleep 2000

# $ kill -SIGHUP %1
# [1]  + 18653 hangup     sleep 1000

# $ jobs
# [2]  + running    nohup sleep 2000

# $ kill -SIGHUP %2

# $ jobs
# [2]  + running    nohup sleep 2000

# $ kill %2
# [2]  + 18745 terminated  nohup sleep 2000

# $ jobs

# nohup sleep 2000 & (the process will keep running in the background)



#tmux (Terminal Multiplexer) is a command-line tool that lets you run and manage multiple terminal 
#sessions inside a single window — and even keep them running after you disconnect.


# ls -la            for your latest runned commands
# CTRL A+D          to detach from tmux

# tmux starts a new session.
# tmux new -s NAME starts it with that name.
# tmux ls lists the current sessions
# Within tmux typing CTRL+A d detaches the current session
# tmux a attaches the last session. You can use -t flag to specify which


# Windows - Equivalent to tabs in editors or browsers, they are visually separate parts of the same session
# CTRL+A c Creates a new window. To close it you can just terminate the shells doing <C-d>
# CTRL+A N Go to the N th window. Note they are numbered
# CTRL+A p Goes to the previous window
# CTRL+A n Goes to the next window
# CTRL+A , Rename the current window
# CTRL+A w List current windows



# Panes - Like vim splits, panes let you have multiple shells in the same visual display.
# <C-b> " Split the current pane horizontally
# <C-b> % Split the current pane vertically
# <C-b> <direction> Move to the pane in the specified direction. Direction here means arrow keys.
# <C-b> z Toggle zoom for the current pane
# <C-b> [ Start scrollback. You can then press <space> to start a selection and <enter> to copy that selection.
# <C-b> <space> Cycle through pane arrangements.



# Aliases
# It can become tiresome typing long commands that involve many flags or verbose options. For this reason, most shells support aliasing. A shell alias is a short form for another command that your shell will replace automatically for you. For instance, an alias in bash has the following structure:

# alias alias_name="command_to_alias arg1 arg2"


# # Make shorthands for common flags
# alias ll="ls -lh"

# # Save a lot of typing for common commands
# alias gs="git status"
# alias gc="git commit"
# alias v="vim"

# # Save you from mistyping
# alias sl=ls

# # Overwrite existing commands for better defaults
# alias mv="mv -i"           # -i prompts before overwrite
# alias mkdir="mkdir -p"     # -p make parent dirs as needed
# alias df="df -h"           # -h prints human readable format

# # Alias can be composed
# alias la="ls -A"
# alias lla="la -l"

# # To ignore an alias run it prepended with \
# \ls
# # Or disable an alias altogether with unalias
# unalias la

# # To get an alias definition just call it with alias
# alias ll
# # Will print ll='ls -lh'


# 1. Bash
# Files:
# ~/.bashrc

# Runs every time you start a new interactive shell (like opening a terminal tab).

# You put aliases, environment variables, and functions here.

# Example:


# alias ll="ls -lah"
# export PATH="$HOME/bin:$PATH"
# ~/.bash_profile (or ~/.profile on some systems)

# Runs once at login (for login shells).

# Often loads ~/.bashrc so settings are consistent.

# Example:

# if [ -f ~/.bashrc ]; then
#     source ~/.bashrc
# fi


# 2. Git
# File:
# ~/.gitconfig

# Stores global Git settings (name, email, aliases, colors).

# Example:

# ini

# [user]
#     name = Sohaib Azhar
#     email = sohaib@example.com
# [alias]
#     st = status
#     co = checkout
#     cm = commit -m
# [color]
#     ui = auto


# 3. Vim
# Files:
# ~/.vimrc

# Main config file for Vim — controls keybindings, colors, indentation, etc.

# Example:

# vim

# syntax on
# set number
# set tabstop=4
# set expandtab
# ~/.vim/ folder

# Stores Vim plugins, colorschemes, and other custom files.

# 4. SSH
# File:
# ~/.ssh/config

# Lets you store shortcuts and configs for SSH connections.

# Example:

# ssh

# Host myserver
#     HostName 192.168.1.10
#     User sohaib
#     Port 2222
#     IdentityFile ~/.ssh/id_rsa
# Then you can just type:
# ssh myserver




# 5. Tmux
# File:
# ~/.tmux.conf

# Customizes Tmux’s behavior and keybindings.

# Example:

# tmux

# set -g mouse on
# set -g history-limit 10000
# bind r source-file ~/.tmux.conf \; display-message "Reloaded!"
# ✅ In short:

# Tool	Config File	Purpose
# Bash	~/.bashrc, ~/.bash_profile	Shell environment & startup scripts
# Git	~/.gitconfig	Git global settings
# Vim	~/.vimrc, ~/.vim/	Editor customization
# SSH	~/.ssh/config	SSH connection shortcuts
# Tmux	~/.tmux.conf	Terminal multiplexer customization
