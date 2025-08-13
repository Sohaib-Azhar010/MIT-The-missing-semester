import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, but I am not stopping")

signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print("\r{}".format(i), end="")
    i += 1



# TOPICS :    1.JOB CONTROL           2.TERMINAL MULTIPLEXER         3.DOT FILES
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