#!/usr/bin/env python

import curses
import time

def draw_art(stdscr):
    # Clear screen
    stdscr.clear()

    # Set up the window
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking

    # Define some ASCII art
    ascii_art = [
        "  ___  ",
        " / _ \\ ",
        "| | | |",
        "| |_| |",
        " \\___/ "
    ]

    patate = "/-\|"

    # Main loop
    pos = [0, 0]
    bar = 0
    while True:
        # Prepare the screen in memory
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        start_y = height // 2 - len(ascii_art) // 2
        start_x = width // 2 - len(ascii_art[0]) // 2

        stdscr.addstr(5, 5, patate[bar])
        bar += 1
        bar %= len(patate)

        for i, line in enumerate(ascii_art):
            stdscr.addstr(start_y + i, start_x, line)

        stdscr.addstr(pos[1], pos[0], "x")
        
        # Refresh the screen with the new content
        stdscr.refresh()

        # Check for user input to exit
        key = stdscr.getch()
        if key == ord('f'):
            break
        if key == ord("s"):
            pos[1] += 1
        if key == ord("z"):
            pos[1] -= 1
        if key == ord("d"):
            pos[0] += 1
        if key == ord("q"):
            pos[0] -= 1
        pos[0] %= width
        pos[1] %= height

        # Add a small delay to control the frame rate
        time.sleep(0.05)

def main():
    curses.wrapper(draw_art)

if __name__ == "__main__":
    main()
