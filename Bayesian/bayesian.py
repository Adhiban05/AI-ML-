from pomegranate import BayesianNetwork, Node

# Create the nodes in the network
A = Node("A", ["Sunny", "Rainy"])
B = Node("B", ["Umbrella", "No Umbrella"])
C = Node("C", ["Wet", "Dry"])

# Define the conditional probability tables
A.conditional_probabilities = [[0.7, 0.3], [0.3, 0.7]]
B.conditional_probabilities = [[0.9, 0.1], [0.1, 0.9]]
C.conditional_probabilities = [[0.8, 0.2], [0.2, 0.8]]

# Add the nodes to the network
network = BayesianNetwork()
network.add_nodes(A, B, C)

# Connect the nodes
network.add_edge(A, B)
network.add_edge(B, C)

# Learn the parameters of the network
network.learn()

# Make a prediction
prediction = network.predict(evidence={"A": "Sunny"})
print(prediction)
