# Fantasy Map Generator

### What it does

Create a map for your Dungeons & Dragons campaign or any of your fantasy map needs!

## How to use it

The python UI will (user.py) will prompt you with several questions to produce a map.jgr file and will then instruct you on how to transform that file into map.jpg.

You'll need to look at the Grid.jpg file to know what coordinates to put in when prompted. If you need help with this, I've generated 3 example input files.
You can use them like so: `python user.py < input1.txt`

Here's an example output for

- Option 1 (Grassland): ![Grassland Example](/Example1.jpg)
- Option 2 (Desert): ![Desert Example](/Example2.jpg)
- Option 3 (Ocean): ![Ocean Example](/Example3.jpg)

This repository should have everything you need to run .jgr files. If you have any issues, please refer to [Dr. James Plank's write up](https://web.eecs.utk.edu/~jplank/plank/classes/cs494/494/notes/Jgraph/lecture.html).

## Issues/Questions

If you have any issues understanding the JGraph code, please refer to the [man page](https://manpages.debian.org/jessie/jgraph/jgraph.1.en.html)

## Features to be added:

These might not all be created with JGraph as it's a challenging language to make pictures with.

- Rivers: I had a lot issues getting the river to ratio properly.
- Volcanoes
- Animals
