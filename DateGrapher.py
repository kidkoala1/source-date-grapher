import re
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import sys


# Extract dates from input.txt, and write to output.txt. 
def extract_dates(input_file, output_file, start_year): 
    current_year = datetime.now().year
    valid_dates = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            matches = re.findall(r'\(?\d{4}\)?|\b\d{4}\b', line)  # Look for 4 digit numbers, with or without brackets. 
            for match in matches:
                year = int(re.sub(r'[^\d]', '', match)) # Remove brackets if present
                if start_year <= year <= current_year:
                    valid_dates.append(str(year))
                    break   # Stop after the first valid year in line
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(valid_dates) + '\n')


# Sort entries ascending
def sort_entries(input):
        with open(input, 'r') as f:
            years = [int(line.strip()) for line in f]

        return(sorted(years))


# Count source occurence per year, and plot in graph
def plot_graph(sorted_years, x_steps):
    counts = Counter(sorted_years)
    years = list(counts.keys())
    frequencies = list(counts.values())

    plt.bar(years, frequencies)
    plt.xlabel("Year source")
    plt.ylabel("Frequency cited")
    plt.title("Source occurences by year")
    plt.yticks(range(0, max(frequencies) + 1, 1)) # Y axis ticks in steps of 1, up to highest occuring frequency
    plt.xticks(range(round_down(min(years)), max(years), x_steps))    # X axis covers the oldest year rounded down to 5, to most recent year.
    plt.show()

# Round down year to nearest 5, used to avoid starting graph at uneven year.
def round_down(year):
    return year // 5 * 5

def print_help():
    help_message = """
    Usage: python DateGrapher.py <input_file> <start_year> <x_steps>
    
    Parameters:
    <input_file>  : Path to the input file containing source list with dates from Wikipedia.
    <start_year>  : The earliest valid year for sources to be extracted. Articles covering older events likely require a lower value.
    <x_steps>     : The step size for the x-axis in the plot. Older articles may require larger steps for readability.
    
    Example:
    python DateGrapher.py input.txt 1900 5
    """
    print(help_message)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_help()
        sys.exit(1)
    
    input_file = sys.argv[1]
    start_year = int(sys.argv[2])
    x_steps = int(sys.argv[3])
    output_file = "output.txt"
    
    extract_dates(input_file, output_file, start_year)
    sorted_years = sort_entries(output_file)
    plot_graph(sorted_years, x_steps)