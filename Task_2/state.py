
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
    def __init__(self, on, clear, blocks, floors, allowed_on, adjacent, goal_state):
        self.on = on  # Dict of block positions
        self.clear = clear  # Dict indicating if a block or floor is clear
        self.blocks = blocks
        self.floors = floors
        self.allowed_on = allowed_on
        self.adjacent = adjacent
        self.goal_state = goal_state

    # Checks if the current state matches the goal state.
    def is_goal(self):
        for block in self.goal_state['on']:
            if self.on.get(block) != self.goal_state['on'][block]:
                return False
        return True

    def get_possible_actions(self):
        actions = []
        for block in self.blocks:
            if self.clear[block]:
                from_pos = self.on[block]
                # Consider moving to floors
                for floor in self.floors:
                    if floor != from_pos and self.clear.get(floor, False) and floor in self.allowed_on[block]:
                        if self.is_adjacent(from_pos, floor):
                            actions.append(Action(block, from_pos, floor))
                # Consider moving onto other blocks
                for dest_block in self.blocks:
                    if dest_block != block and self.clear[dest_block]:
                        if dest_block in self.allowed_on[block]:
                            # Ensure adjacency when moving onto blocks
                            if self.is_adjacent(from_pos, dest_block):
                                actions.append(Action(block, from_pos, dest_block))
        return actions

    # Checks if two positions are on adjacent floors
    def is_adjacent(self, pos1, pos2):
        floor1 = self.get_floor(pos1)
        floor2 = self.get_floor(pos2)
        if floor1 is None or floor2 is None:
            return False
        return floor2 in self.adjacent.get(floor1, [])

    # Recursively finds the floor a block is on
    def get_floor(self, pos):
        if pos in self.floors:
            return pos
        else:
            below = self.on.get(pos)
            if below is None:
                return None
            return self.get_floor(below)

    # Creates a new state if the action is valid
    def apply_action(self, action):
        # Check if action is valid
        if not self.clear[action.block]:  # Cannot move a block that has something on top of it
            return None
        if self.on[action.block] != action.from_pos:  # Ensures the block is where we expect
            return None
        if action.to_pos in self.blocks and not self.clear[action.to_pos]:  # Cannot move onto an occupied block
            return None
        if action.to_pos not in self.allowed_on[action.block]:  # Checks allowed_on constraints
            return None
        # If moving to a floor or block, check adjacency
        if action.to_pos in self.floors or action.to_pos in self.blocks:
            if not self.is_adjacent(action.from_pos, action.to_pos):
                return None  # Action is invalid if positions are not adjacent
        # Create a new state
        new_on = self.on.copy()
        new_clear = self.clear.copy()
        # Update positions
        new_on[action.block] = action.to_pos
        # Update clear statuses
        new_clear[action.block] = True
        new_clear[action.from_pos] = True
        new_clear[action.to_pos] = False
        # If from_pos is a block and no other block is on it, set it to clear
        if action.from_pos in self.blocks:
            is_block_below = any(
                b for b in self.blocks if b != action.block and self.on.get(b) == action.from_pos
            )
            if not is_block_below:
                new_clear[action.from_pos] = True
        return State(new_on, new_clear, self.blocks, self.floors, self.allowed_on, self.adjacent, self.goal_state)

    # Returns a string representation of the state
    def __repr__(self):
        return f"State(on={self.on}, clear={self.clear})"

    # Checks if two states are equal
    def __eq__(self, other):
        return self.on == other.on and self.clear == other.clear

    # Returns a hash value for the state
    def __hash__(self):
        return hash(frozenset(self.on.items())) ^ hash(frozenset(self.clear.items()))