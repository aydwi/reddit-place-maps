## Plots of color data from r/place

'Place' datasets contain a total of 16 colors used throughout the grid. The colors used and their corresponding hex-codes are listed [here](https://redd.it/6640ru).

For a particular color, the script plots the coordinates where it was placed (irrespective of number of times it was placed there), thus showing the regions dominated by the color. Since there are a lot of points, plotting them as **Hexbins** or a **2D-Histogram** seems more appropriate. The input is a CSV file containing a unique list of the specified color's coordinates as `x,y`.

### Processing the data-

  * The bash script `process.sh` generates the required CSV. It accepts two arguments, and can be run by
  
    `chmod +x process.sh`
    
    `./process.sh <path/to/main_file.csv> <color_index>`
    
    See [this post](https://redd.it/6640ru) for the color index of a color.
