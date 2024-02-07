import matplotlib.pyplot as plt

# Function to generate arithmetic progression
def generate_ap(start, common_diff, n):
    ap = [start + i * common_diff for i in range(n)]
    return ap

# Set the starting point, common difference, and number of terms
start_value = 100
common_difference = 1
num_terms = 10  # You can adjust the number of terms as per your requirement

# Generate arithmetic progression
ap_sequence = generate_ap(start_value, common_difference, num_terms)

# Plot the AP
plt.plot(ap_sequence, marker='o', linestyle='-')
plt.title('Arithmetic Progression')
plt.xlabel('Term Number (n)')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('fig1.png')

