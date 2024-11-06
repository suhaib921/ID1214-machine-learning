from collections import deque
import copy


# Define the Blocks and Floors
blocks = ['A', 'B', 'C']
floors = ['Floor1', 'Floor2', 'Floor3']

# Constrains Blocks movements between floors
adjacent = {
    'Floor1': ['Floor2'],
    'Floor2': ['Floor1', 'Floor3'],
    'Floor3': ['Floor2']
}

# Constraints relationships between blocks
allowed_on = {
    'A': ['B', 'C', 'Floor1', 'Floor2', 'Floor3'], #A can be placed on top of B and C in all floors
    'B': ['C', 'Floor1', 'Floor2', 'Floor3'],  #B can be placed on top of C in all floors. A.K.A not on of A
    'C': ['Floor1', 'Floor2', 'Floor3']     #C can be placed in all floors. A.K.A not on of A & B
}

# Define the initial state
initial_state = {
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
goal_state = {
    'on': {
        'A': 'B',
        'B': 'C',
        'C': 'Floor3'
    }
}

# Define the Action class
class Action:
    def __init__(self, block, from_pos, to_pos):
        self.block = block
        self.from_pos = from_pos
        self.to_pos = to_pos
    
    def __repr__(self):
        return f"move({self.block}, {self.from_pos}, {self.to_pos})"

# Define the State class
class State:
    def __init__(self, on, clear):
        self.on = on  # Dict of block positions
        self.clear = clear  # Dict indicating if a block or floor is clear

    #Checks if the current state matches the goal state.
    def is_goal(self):
        for block in goal_state['on']:
            if self.on.get(block) != goal_state['on'][block]:
                return False
        return True

    def get_possible_actions(self):
        actions = []
        for block in blocks:
            if self.clear[block]:
                from_pos = self.on[block]
                # Consider moving to floors
                for floor in floors:
                    if floor != from_pos and self.clear[floor] and floor in allowed_on[block]:
                        if self.is_adjacent(from_pos, floor):
                            actions.append(Action(block, from_pos, floor))
                # Consider moving onto other blocks
                for dest_block in blocks:
                    if dest_block != block and self.clear[dest_block]:
                        if dest_block in allowed_on[block]:
                            actions.append(Action(block, from_pos, dest_block))
        return actions

    #before moving checks if two positions are on adjacent floors(floors besides eachother)
    def is_adjacent(self, pos1, pos2):
        floor1 = self.get_floor(pos1)
        floor2 = self.get_floor(pos2)
        return floor2 in adjacent.get(floor1, [])
    
    #Recursively finds the floor a block is on
    def get_floor(self, pos):
        if pos in floors:
            return pos
        else:
            below = self.on.get(pos)
            return self.get_floor(below)

    # Create a new state if the action is valid
    def apply_action(self, action):
        # Check if action is valid
        if not self.clear[action.block]: #Cannot move a block that has something on top of it.
            return None
        if self.on[action.block] != action.from_pos: #Ensures the block is actually where we think it is
            return None
        if action.to_pos in blocks and not self.clear[action.to_pos]: #Cannot move onto an occupied block or floor
            return None
        if action.to_pos not in allowed_on[action.block]: #Checks against allowed_on constraints
            return None
        if action.to_pos in floors: #If moving to a floor, it must be adjacent to the current floor.
            if not self.is_adjacent(action.from_pos, action.to_pos):
                return None
        # Create a new state
        new_on = self.on.copy()
        new_clear = self.clear.copy()
        # Update positions
        new_on[action.block] = action.to_pos
        # Update clear statuses
        new_clear[action.block] = True
        new_clear[action.from_pos] = True
        if action.to_pos in blocks or action.to_pos in floors:
            new_clear[action.to_pos] = False
        # If from_pos is a block and no other block is on it, set it to clear
        if action.from_pos in blocks:
            if action.block == self.on.get(action.from_pos):
                new_clear[action.from_pos] = True
        return State(new_on, new_clear)

    #Returns a string representation of the state
    def __repr__(self):
        return f"State(on={self.on}, clear={self.clear})"

    #Checks if two states are equal.
    def __eq__(self, other):
        return self.on == other.on and self.clear == other.clear
    
    #Returns a hash value for the state
    def __hash__(self):
        return hash(frozenset(self.on.items())) ^ hash(frozenset(self.clear.items()))

# Simple BFS Planner
def plan(initial_state):
    initial_state_obj = State(initial_state['on'], initial_state['clear'])
    frontier = deque()
    frontier.append((initial_state_obj, []))
    explored = set()

    while frontier:
        current_state, actions = frontier.popleft()
        if current_state.is_goal():
            return actions
        explored.add(current_state)
        for action in current_state.get_possible_actions():
            new_state = current_state.apply_action(action)
            if new_state and new_state not in explored:
                frontier.append((new_state, actions + [action]))
    return None

# Run the planner
actions = plan(initial_state)

# Print the plan
if actions:
    print("Plan found:")
    for i, action in enumerate(actions):
        print(f"Step {i + 1}: {action}")
else:
    print("No plan found.")
