def turtle_a_step(this_turtle):
    """Moves forward and spawns two turtles at different angles."""
    this_turtle.move(50 * this_turtle.health)
    child = this_turtle.copy()
    child.rotate_relative(-20)
    child.health = child.health * child.decay

    this_turtle.rotate_relative(45)
    this_turtle.health = this_turtle.health * this_turtle.decay

    return [this_turtle, child]

def turtle_b_step(this_turtle):
    """Moves forward and spawns two turtles at different angles."""
    this_turtle.move(50 * this_turtle.health)
    child = this_turtle.copy()
    child.rotate_relative(-20)
    child.health = child.health * child.decay
    child.kind = "C"

    this_turtle.rotate_relative(45)
    this_turtle.health = this_turtle.health * this_turtle.decay

    return [this_turtle, child]

def turtle_c_step(this_turtle):
    """Moves forward and spawns two turtles at different angles."""
    this_turtle.move(25 * this_turtle.health)
    this_turtle.health = this_turtle.health * this_turtle.decay

    return [this_turtle]




types_to_steps = {"A": turtle_a_step,
                  "B": turtle_b_step,
                  "C": turtle_c_step}