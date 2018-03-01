## Plots of color data from r/place

'Place' datasets contain a total of 16 colors used throughout the grid. The colors used and their corresponding hex-codes are listed [here](https://redd.it/6640ru).

For a particular color, the scripts plot the points where it was placed (irrespective of number of times it was placed there). Since there are a lot of points, plotting them as **Hexbins** or a **2D-Histogram** seems more appropriate. The input is a CSV file containing a unique list of the specified color's coordinates as `x,y`.

### Processing the data-

  * The bash script `process.sh` can be run to generate the required CSV. It accepts two arguments, and can be run as follows-
  
    `chmod +x process.sh`
    
    `./process.sh <path/to/main_file.csv> <color_number>`
