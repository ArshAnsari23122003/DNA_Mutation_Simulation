# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set parameters
lambda_per_1000_nucleotides = 2  # Mutation rate
strand_length = 10000  # Total length of the DNA strand
num_chunks = strand_length // 1000  # Number of chunks of 1000 nucleotides

# Simulate mutations using Poisson distribution
mutations_per_chunk = np.random.poisson(lambda_per_1000_nucleotides, num_chunks)

# Calculate cumulative mutations
cumulative_mutations = np.cumsum(mutations_per_chunk)

# Create output folder for visuals and data
import os

output_folder = r'C:\Users\HP\OneDrive\Documents\Desktop\DNA_Mutation_Simulation\outputs'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# Plot mutation events along the DNA strand
plt.figure(figsize=(12, 6))
plt.bar(range(1, num_chunks + 1), mutations_per_chunk, color='skyblue', alpha=0.8)
plt.title("Mutations Along the DNA Strand")
plt.xlabel("Chunk Number (1000 Nucleotides Each)")
plt.ylabel("Number of Mutations")
plt.xticks(range(1, num_chunks + 1, 5))  # Adjust x-axis labels for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(f"{output_folder}mutations_along_dna_strand.png")  # Save the plot
plt.show()

# Plot the distribution of mutations
plt.figure(figsize=(10, 6))
sns.histplot(mutations_per_chunk, bins=range(0, max(mutations_per_chunk) + 2), kde=False, color='coral')
plt.title("Distribution of Mutation Counts")
plt.xlabel("Number of Mutations per 1000 Nucleotides")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(f"{output_folder}mutation_distribution.png")  # Save the histogram
plt.show()

# Plot cumulative mutations along the DNA strand
plt.figure(figsize=(12, 6))
plt.plot(range(1, num_chunks + 1), cumulative_mutations, marker='o', color='green')
plt.title("Cumulative Mutations Along the DNA Strand")
plt.xlabel("Chunk Number (1000 Nucleotides Each)")
plt.ylabel("Cumulative Number of Mutations")
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.savefig(f"{output_folder}cumulative_mutations.png")  # Save the cumulative plot
plt.show()

# Save mutation data to CSV
mutation_data = pd.DataFrame({
    "Chunk Number": range(1, num_chunks + 1),
    "Mutations": mutations_per_chunk,
    "Cumulative Mutations": cumulative_mutations
})
mutation_data.to_csv(f"{output_folder}mutation_data.csv", index=False)

# Outputs folder location
output_folder
