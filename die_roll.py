import random
import sys


def roll_die(num_rolls=1000):
    """
    Simulate rolling a 6-sided die num_rolls times
    Using random numbers between 0 and 1 and fractional intervals.
    """
    results = []
    # Define the fraction representing one side of the die
    fraction_interval = 1 / 6

    for _ in range(num_rolls):
        # Generate random number between 0.0 (inclusive) and 1.0 (exclusive)
        rand_num = random.random()  # UPDATED: Use random.random() for 0-1 range

        # Map the random number to a die face (1-6) using fractional intervals
        if 0 <= rand_num < fraction_interval:  # Interval 1: [0, 1/6)
            face = 1
        elif (
            fraction_interval <= rand_num < 2 * fraction_interval
        ):  # Interval 2: [1/6, 2/6)
            face = 2
        elif (
            2 * fraction_interval <= rand_num < 3 * fraction_interval
        ):  # Interval 3: [2/6, 3/6)
            face = 3
        elif (
            3 * fraction_interval <= rand_num < 4 * fraction_interval
        ):  # Interval 4: [3/6, 4/6)
            face = 4
        elif (
            4 * fraction_interval <= rand_num < 5 * fraction_interval
        ):  # Interval 5: [4/6, 5/6)
            face = 5
        else:  # rand_num >= 5 * fraction_interval                 # Interval 6: [5/6, 1.0)
            face = 6

        results.append(face)

    return results


def analyze_results(results):
    """Analyze the frequency and percentage of each face"""
    # Count occurrences of each face
    face_counts = {face: results.count(face) for face in range(1, 7)}

    # Calculate percentages
    total_rolls = len(results)
    if total_rolls == 0:  # Handle case with no rolls
        return {i: 0 for i in range(1, 7)}, {i: 0.0 for i in range(1, 7)}

    face_percentages = {
        face: (count / total_rolls) * 100 for face, count in face_counts.items()
    }

    return face_counts, face_percentages


def print_results_table(face_counts, face_percentages, total_rolls):
    """Print a formatted table of results"""
    # Table header
    print(
        # UPDATED: Description reflects the 0-1 range
        f"\nDie Roll Simulation Results ({total_rolls} rolls using random numbers between 0 and 1)"
    )
    print("=" * 60)
    print(f"{'Face':<10}{'Frequency':<15}{'Percentage (%)':<15}")
    print("-" * 60)

    # Table data
    for face in range(1, 7):
        # Use .get() for safety in case results list was empty or unusual
        count = face_counts.get(face, 0)
        percentage = face_percentages.get(face, 0.0)
        print(
            f"{face:<10}{count:<15}{percentage:.2f}%"
        )  # Using .get ensures this won't error

    # Total row
    print("-" * 60)
    total_percentage = sum(face_percentages.values())  # Calculate sum for display
    # Format total percentage like the others
    print(f"{'Total':<10}{total_rolls:<15}{total_percentage:.2f}%")
    print("=" * 60)


def main():
    # No fixed random seed - results will be different each time
    num_rolls_to_simulate = 1000  # Define number of rolls

    # Simulate die rolls
    results = roll_die(num_rolls_to_simulate)

    # Analyze results
    face_counts, face_percentages = analyze_results(results)

    # Print tables to console
    print_results_table(face_counts, face_percentages, len(results))

    # Also save to file
    original_stdout = sys.stdout
    output_filename = "die_simulation_results.txt"
    try:
        with open(output_filename, "w") as f:
            sys.stdout = f
            # Write header consistent with console output
            print(
                # UPDATED: Description reflects the 0-1 range
                f"Die Roll Simulation Results ({len(results)} rolls using random numbers between 0 and 1)"
            )
            # Call the print table function again to write table to file
            print_results_table(face_counts, face_percentages, len(results))

    except IOError as e:
        # Restore stdout before printing error message
        sys.stdout = original_stdout
        print(f"\nError: Could not write to file {output_filename}. Reason: {e}")
        # Exit or handle error appropriately if needed
        # sys.exit(1)
    else:
        # Restore stdout only if file writing was successful
        sys.stdout = original_stdout
        print(f"\nResults also saved to {output_filename}")
    finally:
        # Ensure stdout is restored even if unexpected errors occur (optional safety net)
        if sys.stdout != original_stdout:
            sys.stdout = original_stdout


if __name__ == "__main__":
    main()
