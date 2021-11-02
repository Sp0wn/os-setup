#!/bin/sh

FILE=~/.config/.target.txt

if [ -f "$FILE" ]; then
    echo "%{F#f42310}什 %{F#ffffff}$(/usr/bin/cat ~/.config/.target.txt)"
else
    echo "%{F#f42310}什%{u-} No target"
fi

