states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

colors = ['Red', 'Green', 'Blue']


neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  [] 
}


def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve_map_coloring(assignment={}):
    if len(assignment) == len(states):
        return assignment
    

    unassigned_states = [s for s in states if s not in assignment]
    current_state = unassigned_states[0]

    for color in colors:
        if is_valid(current_state, color, assignment):

            assignment[current_state] = color
            
            result = solve_map_coloring(assignment)
            if result:
                return result
    
            del assignment[current_state]

    return False

solution = solve_map_coloring()

if solution:
    print("Map successfully colored!")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("No solution found.")