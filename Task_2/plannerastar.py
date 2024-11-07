import heapq

def heuristic(state):
    misplaced_blocks = sum(
        1 for block in state.goal_state['on']
        if state.on.get(block) != state.goal_state['on'][block]
    )
    return misplaced_blocks

def plan(initial_state_obj):
    frontier = []
    heapq.heappush(frontier, (0, 0, initial_state_obj, []))  # (f_score, state_counter, state, actions)
    explored = set()
    state_counter = 0  # To avoid comparison errors in heap when f_scores are equal
    states_explored = 0  # Counter for states explored

    while frontier:
        f_score, _, current_state, actions = heapq.heappop(frontier)
        if current_state.is_goal():
            return actions, states_explored
        explored.add(current_state)
        states_explored += 1
        for action in current_state.get_possible_actions():
            new_state = current_state.apply_action(action)
            if new_state and new_state not in explored:
                g_score = len(actions) + 1  # Assuming each action has a cost of 1
                h_score = heuristic(new_state)
                f_score = g_score + h_score
                state_counter += 1
                heapq.heappush(frontier, (f_score, state_counter, new_state, actions + [action]))
    return None, states_explored