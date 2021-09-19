#!/usr/bin/env python3

import getopt
import sys
import os
from i3ipc import Connection, Event

last_split = "h"

def print_help():
    print("Usage: " + sys.argv[0] + " [-p path/to/pid.file]")
    print("")
    print("Options:")
    print("    -p path/to/pid.file   Saves the PID for this program in the filename specified")
    print("")


def find_parent(i3, window_id):
    """
        Find the parent of a given window id
    """

    def finder(con, parent):
        if con.id == window_id:
            return parent
        for node in con.nodes:
            res = finder(node, con)
            if res:
                return res
        return None

    return finder(i3.get_tree(), None)


def set_layout(i3, _):
    """
        Set the layout/split for the currently
        focused window to either vertical or
        horizontal, depending on its width/height
    """

    """
        NOTE: if you only want to monitor splits
        without automatically changing them,
        comment out the two i3.command lines
        and replace
        `elif win.rect.height > win.rect.width:`
        with
        `elif parent.layout == "splitv":`
    """
    win = i3.get_tree().find_focused()
    parent = find_parent(i3, win.id)

    if parent:
        if parent.layout in ("tabbed", "stacked"):
            print_status(parent.layout)
        elif win.rect.height > win.rect.width:
            i3.command('split v')
            print_status("v")
        else:
            i3.command('split h')
            print_status("h")


def print_status(split):
    global last_split

    if split == "v":
        print(" ↓")
        last_split = "v"
    elif split == "h":
        print("→")
        last_split = "h"
    elif split == "tabbed":
        print(" t")
    elif split == "stacked":
        print(" s")
    elif split == "t":
        # for split toggle
        if last_split == "h":
            print_status("v")
        else:
            print_status("h")


def keybind_hook(i3, e):
    cmd, *args = e.binding.command.split()
    if cmd == "split":
        print_status(args[0][0])
    elif cmd == "layout":
        if args[0][:-1] == "split":
            print_status(args[0][-1])
        else:
            print_status(args[0])
    elif cmd == "move":
        set_layout(i3, e)


def main():
    """
    Main function - listen for window focus
        changes and call set_layout when focus
        changes
    """
    opt_list, _ = getopt.getopt(sys.argv[1:], 'hp:')
    pid_file = None
    for opt in opt_list:
        if opt[0] == "-h":
            print_help()
            sys.exit()
        if opt[0] == "-p":
            pid_file = opt[1]

    if pid_file:
        with open(pid_file, 'w') as f:
            f.write(str(os.getpid()))

    i3 = Connection()
    i3.on(Event.WINDOW_FOCUS, set_layout)
    i3.on(Event.BINDING, keybind_hook)
    set_layout(i3, "")
    i3.main()


if __name__ == "__main__":
    main()
