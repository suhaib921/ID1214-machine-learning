import java.util.*;

public class BlocksWorldSTRIPS {

    // Define predicates
    static class State {
        Set<String> predicates;

        public State() {
            predicates = new HashSet<>();
        }

        public State(State other) {
            predicates = new HashSet<>(other.predicates);
        }

        public void add(String predicate) {
            predicates.add(predicate);
        }

        public void remove(String predicate) {
            predicates.remove(predicate);
        }

        public boolean contains(String predicate) {
            return predicates.contains(predicate);
        }

        public boolean satisfies(Set<String> goals) {
            return predicates.containsAll(goals);
        }

        @Override
        public String toString() {
            return predicates.toString();
        }
    }

    // Define action schema
    static class Action {
        String name;
        Set<String> preconditions;
        Set<String> addList;
        Set<String> deleteList;

        public Action(String name) {
            this.name = name;
            preconditions = new HashSet<>();
            addList = new HashSet<>();
            deleteList = new HashSet<>();
        }

        public boolean isApplicable(State state) {
            return state.predicates.containsAll(preconditions);
        }

        public State apply(State state) {
            State newState = new State(state);
            newState.predicates.removeAll(deleteList);
            newState.predicates.addAll(addList);
            return newState;
        }

        @Override
        public String toString() {
            return name;
        }
    }

    // Planner function
    public static List<Action> plan(State initialState, Set<String> goalState,
                                    List<Action> actions) {
        Queue<Node> frontier = new LinkedList<>();
        Set<State> explored = new HashSet<>();

        frontier.add(new Node(initialState, null, null));

        while (!frontier.isEmpty()) {
            Node node = frontier.poll();
            if (node.state.satisfies(goalState)) {
                return extractPlan(node);
            }
            explored.add(node.state);

            for (Action action : actions) {
                if (action.isApplicable(node.state)) {
                    State childState = action.apply(node.state);
                    if (!explored.contains(childState)) {
                        frontier.add(new Node(childState, node, action));
                    }
                }
            }
        }
        return null;
    }

    static class Node {
        State state;
        Node parent;
        Action action;

        public Node(State state, Node parent, Action action) {
            this.state = state;
            this.parent = parent;
            this.action = action;
        }
    }

    private static List<Action> extractPlan(Node node) {
        List<Action> plan = new ArrayList<>();
        while (node.parent != null) {
            plan.add(0, node.action);
            node = node.parent;
        }
        return plan;
    }

    public static void main(String[] args) {
        // Initial State
        State initialState = new State();
        initialState.add("on(a, b)");
        initialState.add("on(b, c)");
        initialState.add("on(c, Floor1)");
        initialState.add("clear(a)");
        initialState.add("clear(Floor2)");
        initialState.add("clear(Floor3)");
        initialState.add("block(a)");
        initialState.add("block(b)");
        initialState.add("block(c)");
        initialState.add("floor(Floor1)");
        initialState.add("floor(Floor2)");
        initialState.add("floor(Floor3)");
        initialState.add("adjacent(Floor1, Floor2)");
        initialState.add("adjacent(Floor2, Floor1)");
        initialState.add("adjacent(Floor2, Floor3)");
        initialState.add("adjacent(Floor3, Floor2)");

        // Goal State
        Set<String> goalState = new HashSet<>();
        goalState.add("on(a, b)");
        goalState.add("on(b, c)");
        goalState.add("on(c, Floor3)");

        // Actions
        List<Action> actions = createActions();

        // Plan
        List<Action> plan = plan(initialState, goalState, actions);

        // Output the plan
        if (plan != null) {
            System.out.println("Plan found:");
            for (Action action : plan) {
                System.out.println(action);
            }
        } else {
            System.out.println("No plan found.");
        }
    }

    private static List<Action> createActions() {
        List<Action> actions = new ArrayList<>();

        String[] blocks = {"a", "b", "c"};
        String[] positions = {"b", "c", "Floor1", "Floor2", "Floor3"};
        String[] floors = {"Floor1", "Floor2", "Floor3"};

        // Generate move actions
        for (String x : blocks) {
            for (String y : positions) {
                for (String z : positions) {
                    if (!y.equals(z)) {
                        Action action = new Action("move(" + x + ", " + y + ", " + z + ")");
                        action.preconditions.add("clear(" + x + ")");
                        action.preconditions.add("on(" + x + ", " + y + ")");
                        action.preconditions.add("clear(" + z + ")");

                        // Handle adjacency for floors
                        if (isFloor(y) && isFloor(z)) {
                            action.preconditions.add("adjacent(" + y + ", " + z + ")");
                        } else if (isFloor(y) && !isFloor(z)) {
                            action.preconditions.add("adjacent(" + y + ", " + getPosition(z) + ")");
                        } else if (!isFloor(y) && isFloor(z)) {
                            action.preconditions.add("adjacent(" + getPosition(y) + ", " + z + ")");
                        } else {
                            action.preconditions.add("adjacent(" + getPosition(y) + ", " + getPosition(z) + ")");
                        }

                        // Constraints
                        if ((x.equals("b") && z.equals("a")) || (x.equals("c") && (z.equals("a") || z.equals("b")))) {
                            continue; // Invalid move
                        }

                        action.addList.add("on(" + x + ", " + z + ")");
                        action.addList.add("clear(" + y + ")");
                        action.deleteList.add("on(" + x + ", " + y + ")");
                        action.deleteList.add("clear(" + z + ")");

                        actions.add(action);
                    }
                }
            }
        }
        return actions;
    }

    private static boolean isFloor(String position) {
        return position.startsWith("Floor");
    }

    private static String getPosition(String block) {
        // For simplicity, assume blocks can be on floors only
        return "Floor1"; // Placeholder; in a full implementation, track positions dynamically
    }
}
