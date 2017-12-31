## Main plot

This folder contains scripts and data to plot the heatmap of full 1000 x 1000 'Place' grid.

### Processing the initial data

The file `main_file.csv` contains a lot of data. Not all of it is required to plot the map, and therefore it is processed to produce a file `processed.csv`
that the plotting script `plot.py` takes as an input. GNU/Linux command line tools like `grep`, `cut`, `sed` and `awk` are required.

The shell script `process.sh` can be run to perform all the steps and generate the required file. It accepts one parameter, `main_file.csv`

  `chmod +x process.sh`

  `./process.sh <path_to_main_file>`
