# source-date-grapher
DateGrapher extracts dates from a text file (eg Wikipedia sources) and visualizes the frequency of occurance by year in a bar  graph. Made this for a twitter argument

![Figure_1](https://github.com/user-attachments/assets/e8595c14-c9eb-410b-bc0a-3c959d3cf93a)

# Usage
python DateGrapher.py <input_file> <start_year> <x_steps>
    
    Parameters:
    <input_file>  : Path to the input file containing source list with dates from Wikipedia.
    <start_year>  : The earliest valid year for sources to be extracted. Articles covering older events likely require a lower value.
    <x_steps>     : The step size for the x-axis in the plot. Older articles may require larger steps for readability.
    
    Example:
    python DateGrapher.py input.txt 1900 5

# Input file
Made specifically for Wikipedia pages, but works with any input that has:
* 1 source per line
* Source year of origin is the first valid 4 digit number in line

Be careful when using the 'references' on Wikipedia, these often list the same source multiple times. Try to use 'works cited' if available. 
An example input.txt has been provided, sourced from the [Gertie the Dinosaur wiki page](https://en.wikipedia.org/wiki/Gertie_the_Dinosaur).
