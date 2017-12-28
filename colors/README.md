## Plots of color data from r/place

'Place' datasets contain a total of 16 colors used throughout the grid. The colors used and their corresponding hex-codes are listed [here](https://redd.it/6640ru).

For a particular color, the scripts plot the points where it was placed (irrespective of number of times it was placed there). Since there are a lot of points, plotting them as **Hexbins** or a **2D-Histogram** seems more appropriate. The input is a CSV file containing a unique list of the specified color's coordinates as `x,y`.

### Usage-

  * The shell script `process.sh` can be run to generate the required CSV. It takes two arguments, and can be run as follows-
  
    `chmod +x process.sh`
    
    `./process.sh <main_csv_file> <color_code>`
    
    It should be noted that any one of `grep` or `awk` can be used within the script, but using `grep` is slightly faster.
