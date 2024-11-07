from collections import deque 

def plan(initial_state_obj):
    frontier = deque() 
    frontier.append((initial_state_obj, []))
    explored = set() 
    states_explored = 0 

    while frontier:
        current_state, actions = frontier.popleft()
        if current_state.is_goal():
            return actions, states_explored
        explored.add(current_state)
        states_explored += 1
        for action in current_state.get_possible_actions():
            new_state = current_state.apply_action(action)
            if new_state and new_state not in explored:
                frontier.append((new_state, actions + [action]))
    return None, states_explored