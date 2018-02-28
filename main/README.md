## Main plot

Plot the heatmap of full 1000 x 1000 Place grid.

### Processing the data

The file `main_file.csv` contains a large amount of data, not all of which is required to plot the map. Therefore it is processed to produce a file `processed.csv`, which contains the coordinates and their number of placements in the form of `x,y,count`.

The Bash script `process.sh` can be run to perform all the processing and generate the required file. It accepts one parameter, `main_file.csv`. 

    chmod +x process.sh
    
    ./process.sh <path/to/main_file.csv>

### Plotting the map

The Python script `plot.py` plots the heatmap from the data contained in `processed.csv`. It depends on the Python pacakges `numpy`, `pandas` and `matplotlib`, which can be installed using `pip`.

    python3 plot.py
    
The script plots the heatmap and saves it as a PNG image. It can generate a heatmap with or without the points with *zero* placements. Additional options like *colormaps* and *dpi* can be adjusted within the program.
