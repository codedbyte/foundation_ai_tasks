subcounties = [
    'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 'Kibra',
    'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi South', 'Embakasi North',
    'Embakasi Central', 'Embakasi East', 'Embakasi West', 'Makadara',
    'Kamukunji', 'Starehe', 'Mathare'
]

neighbors = {
    'Westlands': ['Dagoretti North', 'Kibra', 'Starehe', 'Mathare', 'Ruaraka'],
    'Dagoretti North': ['Westlands', 'Dagoretti South', 'Kibra'],
    'Dagoretti South': ['Dagoretti North', 'Kibra', 'Langata'],
    'Langata': ['Dagoretti South', 'Kibra', 'Starehe', 'Makadara', 'Embakasi South'],
    'Kibra': ['Dagoretti North', 'Dagoretti South', 'Langata', 'Starehe', 'Westlands'],
    'Roysambu': ['Kasarani', 'Ruaraka'],
    'Kasarani': ['Roysambu', 'Ruaraka', 'Embakasi North', 'Embakasi Central', 'Embakasi East'],
    'Ruaraka': ['Westlands', 'Mathare', 'Roysambu', 'Kasarani', 'Embakasi North'],
    'Embakasi South': ['Langata', 'Makadara', 'Embakasi East'],
    'Embakasi North': ['Ruaraka', 'Kasarani', 'Embakasi Central', 'Mathare'],
    'Embakasi Central': ['Embakasi North', 'Kasarani', 'Embakasi West', 'Embakasi East'],
    'Embakasi East': ['Embakasi Central', 'Kasarani', 'Embakasi South', 'Makadara', 'Embakasi West'],
    'Embakasi West': ['Embakasi Central', 'Makadara', 'Kamukunji', 'Embakasi East'],
    'Makadara': ['Starehe', 'Kamukunji', 'Embakasi West', 'Embakasi East', 'Embakasi South', 'Langata'],
    'Kamukunji': ['Starehe', 'Mathare', 'Makadara', 'Embakasi West'],
    'Starehe': ['Westlands', 'Kibra', 'Langata', 'Makadara', 'Kamukunji', 'Mathare'],
    'Mathare': ['Westlands', 'Starehe', 'Kamukunji', 'Ruaraka', 'Embakasi North']
}

def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(states, colors, assignment):
    if len(assignment) == len(states):
        return assignment

    unassigned_states = [s for s in states if s not in assignment]
    
    unassigned_states.sort(key=lambda s: len(neighbors[s]), reverse=True)
    current_state = unassigned_states[0]

    for color in colors:
        if is_valid(current_state, color, assignment):
            assignment[current_state] = color
            result = solve_map_coloring(states, colors, assignment)
            if result:
                return result

            del assignment[current_state]
            
    return False


color_palettes = [
    ['Red'],
    ['Red', 'Green'],
    ['Red', 'Green', 'Blue'],
    ['Red', 'Green', 'Blue', 'Yellow'],
    ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
]

solution = None
min_colors_needed = 0

for palette in color_palettes:
    assignment = {}
    solution = solve_map_coloring(subcounties, palette, assignment)
    if solution:
        min_colors_needed = len(palette)
        break

if solution:
    print(f"Map successfully colored using a minimum of {min_colors_needed} colors!\n")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("No solution found.")