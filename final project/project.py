import math
import sys

# the 3 wood Wood material elasticity in Pascals units
WOOD_MODULUS = {
    "pine": 11.0e9,
    "oak": 12.4e9,
    "fir": 13.0e9
}

# the limit of when the type of wood gets crushed (Pascals)
WOOD_CRUSH_LIMIT = {
    "pine": 36.2e6,
    "oak": 49.6e6,
    "fir": 42.8e6
}

def main():
    print("--- Abe's Gym Structural Analyzer ---") # titile ;)

    # Get user inputs with quick default options if nothing is entered
    try:
        wood = input("Wood type (pine/oak/fir) [default: pine]: ").strip().lower() or "pine"
        if wood not in WOOD_MODULUS:
            sys.exit("Error: That wood type isn't an option.")

        weight_input = input("Athlete weight in lbs [default: 250]: ").strip()
        weight_lbs = float(weight_input) if weight_input else 250.0
        # Convert lbs to kg for easier calculations
        mass_kg = weight_lbs * 0.453592

        vel_input = input("Landing velocity in m/s [default: 2.0]: ").strip()
        velocity = float(vel_input) if vel_input else 2.0

        posts_number = input("Number of active posts holding the bar (2 or 4) [default: 2]: ").strip()
        active_posts = int(posts_number) if posts_number else 2
        if active_posts not in (2, 4):
            sys.exit("Error: Active posts must be either 2 or 4.")

    except ValueError:
        sys.exit("Error: Please enter valid NUMBERS for weight, velocity, and posts.")

    #  dimensions from my actual backyard gym design layout
    post_height = 2.44        # 8ft in meters
    post_thickness = 0.089   # Standard 4x4 timber (3.5" x 3.5") in meters
    block_width = 0.089      # 4x4 block width in meters
    bar_diameter = 0.0334    # 1" Schedule 40 steel pipe outer diameter (meters)

    # Run the equations for the outputs
    try:
        single_post_limit = calculate_column_buckling(post_thickness, post_height, wood)
        total_impact_force = simulate_dynamic_impact(mass_kg, velocity)

        total_gym_capacity = single_post_limit * active_posts
        force_per_block = total_impact_force / 2.0

        actual_bearing_stress = calculate_bearing_stress(force_per_block, bar_diameter, block_width)
    except ValueError as e:
        sys.exit(f"Calculation Error: {e}")

    # Calculate final safety margins outputs
    allowed_crush = WOOD_CRUSH_LIMIT[wood]
    buckling_safety_factor = total_gym_capacity / total_impact_force
    bearing_safety_factor = allowed_crush / actual_bearing_stress

    # Output the structural data report layout (very clean :0)
    print("\n=== STRUCTURAL SAFETY REPORT ===")
    print(f"Single Post Buckling Limit : {single_post_limit:.1f} N")
    print(f"Total Gym Frame Capacity   : {total_gym_capacity:.1f} N")
    print(f"Peak Dynamic Impact Force  : {total_impact_force:.1f} N")
    print(f"Wood Crushing Stress       : {(actual_bearing_stress / 1e6):.2f} MPa")
    print(f"Buckling Safety Factor     : {buckling_safety_factor:.2f} SF")
    print(f"Bearing Safety Factor      : {bearing_safety_factor:.2f} SF")

    # if the buckling factor is less than 1 then print Danger.... and if hogher print Desien verified......
    if buckling_safety_factor < 1.0 or bearing_safety_factor < 1.0:
        print("\n❌ DANGER: Structural limits breached! The gym will fail under this load.")
    else:
        print("\n✅ DESIGN VERIFIED: The structural frame is completely safe for construction.")


# now the acctual equations


def calculate_column_buckling(thickness, height, wood_type):
    if thickness <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive values.")

    wood = wood_type.lower()
    if wood not in WOOD_MODULUS:
        raise ValueError("Invalid wood species passed to calculator.")

    e_value = WOOD_MODULUS[wood]
    # Moment of inertia for square post: I = width^4 / 12
    inertia_i = (thickness ** 4) / 12.0
    # Euler buckling formula
    return (math.pi ** 2 * e_value * inertia_i) / (height ** 2)


def simulate_dynamic_impact(mass, velocity, stopping_dist=0.02):
    if mass <= 0 or velocity < 0 or stopping_dist <= 0:
        raise ValueError("Mass, velocity, and stopping bounds must be positive numbers.")

    # Work-Energy principle calculation
    kinetic_energy = 0.5 * mass * (velocity ** 2)
    impact_force = kinetic_energy / stopping_dist
    gravity_force = mass * 9.81
    return impact_force + gravity_force


def calculate_bearing_stress(force, bar_dia, block_w):
    if force <= 0 or bar_dia <= 0 or block_w <= 0:
        raise ValueError("Forces and component dimensions must be positive metrics.")

    # Area of contact footprint = bar diameter * block width
    bearing_area = bar_dia * block_w
    return force / bearing_area


if __name__ == "__main__":
    main()
