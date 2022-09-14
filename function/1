"""Modifying a List in a Function"""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simultate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

completed_models = []

# Prevent function from modifying a list by using a copy of the list
print_models(unprinted_designs[:], completed_models)

show_completed_models(completed_models)

