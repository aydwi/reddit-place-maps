## Main plot

This folder contains scripts and data to plot the heatmap of full 1000 x 1000 Place grid.

### Processing the initial data

The file `main_file.csv` contains a lot of data. Not all of it is required to plot the map, and therefore it is processed to produce a file `processed.csv`, which contains the coordinates and their no. of placements in the form of `x,y,count`.

The shell script `process.sh` can be run to perform all the processing and generate the required file. It accepts one parameter, `main_file.csv`. Note that it requires UNIX tools like `cut`, `grep`, `sed` and `awk` to be present. 

#### Running process.sh

    chmod +x process.sh
    
    ./process.sh <path_to_main_file>

### Plotting the map

Now that we have processed data to work with, the Python script `plot.py` can be used to plot the data. It can generate maps with or without the points with *zero* placements.

Note that the Python pacakges `numpy`, `pandas` and `matplotlib` should be present.

    python3 plot.py
    
It plots the map and saves a PNG image of the map. Additional options like *colormaps* and *dpi* can be adjusted within the program.
