# DNA_Mutation_Simulation

Modeling DNA Mutations using Poisson Distribution
This project simulates the occurrence of mutations along a DNA strand using the Poisson distribution. 
The mutations are modeled based on a fixed mutation rate, and the project provides visualizations to understand 
the distribution of mutations along the DNA strand. The purpose of this project is to demonstrate the application 
of the Poisson distribution in a biological context, specifically for modeling rare events such as mutations.

Objective
The objective of this project is to simulate DNA mutations and visualize their distribution along a DNA strand using the Poisson distribution. The main steps involved in the project are:

1. Simulating mutations along a DNA strand using the Poisson distribution.
2. Visualizing the mutations with various plots to understand their distribution.
3. Saving the simulation data for further analysis.

Features
1. Poisson Distribution: The project models mutations as rare events that follow a Poisson distribution with a given mutation rate.

2. Simulations: The program generates random mutation data for chunks of a DNA strand.

3. Visualizations:
a. Bar plots showing the number of mutations in each chunk.
b. Histograms of mutation counts to visualize the distribution.
c. Line plots showing cumulative mutations along the strand.

4. Data Storage: The simulation data, including the number of mutations in each chunk and cumulative mutations, is saved in a CSV file for further analysis.

Requirements
1. Python 3.x
2. Libraries:
a. numpy for generating Poisson-distributed random numbers.
b. matplotlib for plotting graphs and visualizations.
c. seaborn for enhanced visualization.
d. pandas for handling mutation data and exporting it to CSV.

Output
1. Visualization: The following plots will be generated:
a. Mutation Events: A bar plot showing the number of mutations in each chunk of the DNA strand.
b. Mutation Distribution: A histogram visualizing the distribution of mutations.
c. Cumulative Mutations: A line plot showing how mutations accumulate across the strand.
2. CSV Data: The mutation data, including the number of mutations per chunk and cumulative mutations, will be saved in a file mutation_data.csv inside the outputs/ folder.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

This project was inspired by the use of the Poisson distribution in modeling rare biological events like mutations.
Thanks to the open-source Python community for providing the libraries used in this project.
