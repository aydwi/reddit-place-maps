# reddit-place-maps

Visualizing data from the 2017 Reddit event - [Place](https://www.reddit.com/r/place/)


### Obtaining and refining the dataset

Place datasets were publicly released [here](https://redd.it/6640ru). The **full dataset** contains the details of all the tile placements throughout the event, and can be downloaded (as a gzipped CSV) [here](https://storage.googleapis.com/place_events/tile_placements.csv.gz).

The Place canvas was a 1000x1000 grid, but the **full dataset** contains coordinates ranging form [0-1000] instead of [0-999] (possibly due a bug). These extra points are discarded to obtain a refined file `main_file.csv`, which is used as a source of data almost everywhere in this repository. On a UNIX-like system, this can be done by running

    awk -F, '$3<1000 && $4<1000' tile_placements.csv > main_file.csv
    
Here, `tile_placements.csv` is the name of the original (full dataset) file.

### Requirements

* Pandas
* Numpy
* Matplotlib
* seaborn

