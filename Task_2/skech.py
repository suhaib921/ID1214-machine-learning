import time
import networkx as nx
import matplotlib.pyplot as plt
from state import State
from plannerBFS import plan

# Define the Blocks and Floors
blocks = ['A', 'B', 'C']
floors = ['Floor1', 'Floor2', 'Floor3']

# Constraints for block movements between floors
adjacent = {
    'Floor1': ['Floor2'],
    'Floor2': ['Floor1', 'Floor3'],
    'Floor3': ['Floor2']
}

# Constraints relationships between blocks
allowed_on = {
    'A': ['B', 'C', 'Floor1', 'Floor2', 'Floor3'],
    'B': ['C', 'Floor1', 'Floor2', 'Floor3'],
    'C': ['Floor1', 'Floor2', 'Floor3']
}

# Define the initial state
initial_state_data = {
    'on': {
        'A': 'B',
        'B': 'C',
        'C': 'Floor1'
    },
    'clear': {
        'A': True,
        'B': False,
        'C': False,
        'Floor1': False,
        'Floor2': True,
        'Floor3': True
    }
}

# Define the goal state
goal_state_data = {
    'on': {
        'A': 'B',
        'B': 'C',
        'C': 'Floor3'
    }
}

# Create the initial state object
initial_state_obj = State(
    on=initial_state_data['on'],
    clear=initial_state_data['clear'],
    blocks=blocks,
    floors=floors,
    allowed_on=allowed_on,
    adjacent=adjacent,
    goal_state=goal_state_data
)
def generate_problem_space(initial_state):
    G = nx.DiGraph()  # Directed graph
    frontier = [(initial_state, 0)]  # Store tuples of (state, level)
    explored = set()
    state_id_map = {}  # Map state to unique ID for graph nodes

    # Function to create a unique identifier for a state
    def state_to_id(state):
        return state_id_map.setdefault(state, len(state_id_map))

    while frontier:
        current_state, level = frontier.pop(0)
        current_state_id = state_to_id(current_state)

        explored.add(current_state)
        G.add_node(current_state_id, label=f"S{current_state_id}", subset=level)

        for action in current_state.get_possible_actions():
            new_state = current_state.apply_action(action)
            if new_state:
                new_state_id = state_to_id(new_state)
                G.add_node(new_state_id, label=f"S{new_state_id}", subset=level + 1)
                # Use a simplified label by converting `action` to a string or accessing a concise attribute
                G.add_edge(current_state_id, new_state_id, label=str(action))  
                if new_state not in explored and (new_state, level + 1) not in frontier:
                    frontier.append((new_state, level + 1))
    return G, state_id_map

# Generate the problem space graph
G, state_id_map = generate_problem_space(initial_state_obj)

# Define initial and goal state IDs
initial_state_id = state_id_map[initial_state_obj]
goal_state = State(
    on=goal_state_data['on'],
    clear={},  # Replace with actual `clear` values if necessary
    blocks=blocks,
    floors=floors,
    allowed_on=allowed_on,
    adjacent=adjacent,
    goal_state=goal_state_data
)
goal_state_id = state_id_map.get(goal_state, len(state_id_map)-1)  # Approximation

# Highlight the shortest path to the goal if possible
def get_shortest_path_edges(G, start, end):
    try:
        shortest_path = nx.shortest_path(G, source=start, target=end)
        return [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    except nx.NetworkXNoPath:
        return []

# Draw the graph
def draw_graph(G, initial_state_id, goal_state_id):
    pos = nx.spring_layout(G, seed=42, k=1)  # Increased spacing with spring layout

    # Highlight path to goal
    shortest_path_edges = get_shortest_path_edges(G, initial_state_id, goal_state_id)
    edge_colors = ["red" if (u, v) in shortest_path_edges else "black" for u, v in G.edges()]

    # Set node colors to highlight initial and goal states
    node_colors = ['green' if node == initial_state_id else 'red' if node == goal_state_id else 'skyblue' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=800, node_color=node_colors, edgecolors="black")
    
    # Draw node labels (simple labels S0, S1, ...)
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight='bold')

    # Draw edges with color highlighting for shortest path
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, connectionstyle='arc3,rad=0.2', edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

    plt.axis('off')
    plt.show()

# Visualize the improved graph with initial and goal states highlighted
draw_graph(G, initial_state_id, goal_state_id)
