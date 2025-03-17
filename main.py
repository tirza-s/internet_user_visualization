import csv
import matplotlib.pyplot as plt

def generate_population_dictionary(filename):
    """
    Generate population dictionary from the CSV data

        Return a dictionary with the following structure:
        {
        "Africa" : {population : [100, 200, 300], years [1990, 2000, 2010]}
        "Asia    : {population : [300, 500, 800], years [1990, 2000, 2010]}
        }
    """

    population_per_continent = {}

    with open(file_name, "r") as file_reader:
        csv_reader = csv.DictReader(file_reader)
        for line in csv_reader:
            continent = line["continent"]
            year = int(line["year"])
            population = int(line["population"])

            if continent not in population_per_continent:
                population_per_continent[continent] = {
                    "population": [],
                    "years": []
                }

            population_per_continent[continent]["population"].append(
                population)
            population_per_continent[continent]["years"].append(year)

    return population_per_continent
    

def generate_population(population_dictionary): 
    """
    Generate a population plot from the dictionary, 
    creating one plot for each continent.
    """
    for continent in population_dictionary:
        years = population_dictionary[continent]["years"]
        population = population_dictionary[continent]["population"]
        plt.plot(years, population, label=continent, marker="o", alpha=0.75)

    plt.title("Internet population percontinet")
    plt.xlabel("Year")
    plt.ylabel("Internet users")
    plt.grid(True)
    plt.legend()
    plt.show()

file_name = "data.csv"

#Visualize the internet-using population in the plot.
population_per_continent = generate_population_dictionary(file_name)
generate_population(population_per_continent)
