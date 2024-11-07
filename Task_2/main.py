import time
from state import State
from plannerBFS import plan as plan_bfs
from plannerastar import plan as plan_astar

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

# Run BFS Planner 1000 times and measure the average time in microseconds
bfs_total_time = 0
for _ in range(1000):
    start_time_bfs = time.perf_counter()
    actions_bfs, states_explored_bfs = plan_bfs(initial_state_obj)
    end_time_bfs = time.perf_counter()
    bfs_total_time += (end_time_bfs - start_time_bfs)

bfs_average_time_microseconds = (bfs_total_time / 1000) * 1_000_000

# Run A* Planner 1000 times and measure the average time in microseconds
astar_total_time = 0
for _ in range(1000):
    start_time_astar = time.perf_counter()
    actions_astar, states_explored_astar = plan_astar(initial_state_obj)
    end_time_astar = time.perf_counter()
    astar_total_time += (end_time_astar - start_time_astar)

astar_average_time_microseconds = (astar_total_time / 1000) * 1_000_000

# Print the average time taken in microseconds
print(f"\n=== Average Execution Time (1000 runs) ===")
print(f"BFS Planner: {bfs_average_time_microseconds:.2f} microseconds")
print(f"A* Planner: {astar_average_time_microseconds:.2f} microseconds")

# Print the results
print("\n=== BFS Planner Results ===")
actions_bfs, states_explored_bfs = plan_bfs(initial_state_obj)
if actions_bfs:
    print("Plan found using BFS:")
    for i, action in enumerate(actions_bfs):
        print(f"Step {i + 1}: {action}")
    print(f"States explored: {states_explored_bfs}")
else:
    print("No plan found")
  
  
