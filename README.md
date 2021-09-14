i3-alternating-layout
=====================

This fork turns i3-alternating_layout into a polybar module that will inform you of the current split direction. Since the split is usually handled automatically by the script, it's not always useful, but you can disable the split change functionality if you want to keep the manual splits and have your bar inform you of what split you've set for each window.

Scripts to open new windows in i3wm/Sway using alternating layouts (splith/splitv) for each new window. These scripts were made for [/u/ke7ofi](http://www.reddit.com/user/ke7ofi) after they asked a question on how to do this [you can read the question here](http://www.reddit.com/r/i3wm/comments/1sdc39/alternating_horizontal_and_vertical_splitting/).

Installation
------------
```
pip3 install i3ipc
git clone https://github.com/joooooooooooooooooooooooooooooooooooosh/i3-alternating-layout
```

Then add this module to your polybar config and ensure `split` is added to the list of active modules:

```
[module/split]
type = custom/script
exec = python -u /path/to/alternating_layouts.py
tail = true
```

Screenshot
----------

Using regular i3/Sway, creating a window layout like this would involve a lot of `$mod+Return`, `$mod+h` and `$mod+v`. Using this script, you only need to open a bunch of new windows!

![Screenshot](https://github.com/olemartinorg/i3-alternating-layout/raw/master/screenshot.png "Screenshot (1920x1080)")
