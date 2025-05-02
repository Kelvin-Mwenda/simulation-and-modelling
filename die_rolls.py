import random
import sys


def roll_die(num_rolls=1000):
    """
    Simulate rolling a 6-sided die num_rolls times
    Using random numbers between 0 and 10
    """
    results = []
    for _ in range(num_rolls):
        # Generate random number between 0 and 10
        rand_num = random.uniform(0, 10)

        # Map the random number to a die face (1-6)
        # Each face has an equal probability range of 10/6 ≈ 1.67
        if 0 <= rand_num < 10 / 6:  # 0 to ~1.67
            face = 1
        elif 10 / 6 <= rand_num < 2 * (10 / 6):  # ~1.67 to ~3.33
            face = 2
        elif 2 * (10 / 6) <= rand_num < 3 * (10 / 6):  # ~3.33 to ~5.0
            face = 3
        elif 3 * (10 / 6) <= rand_num < 4 * (10 / 6):  # ~5.0 to ~6.67
            face = 4
        elif 4 * (10 / 6) <= rand_num < 5 * (10 / 6):  # ~6.67 to ~8.33
            face = 5
        else:  # ~8.33 to 10
            face = 6

        results.append(face)

    return results


def analyze_results(results):
    """Analyze the frequency and percentage of each face"""
    # Count occurrences of each face
    face_counts = {face: results.count(face) for face in range(1, 7)}

    # Calculate percentages
    total_rolls = len(results)
    face_percentages = {
        face: (count / total_rolls) * 100 for face, count in face_counts.items()
    }

    return face_counts, face_percentages


def print_results_table(face_counts, face_percentages, total_rolls):
    """Print a formatted table of results"""
    # Table header
    print(
        "\nDie Roll Simulation Results (1000 rolls using random numbers between 0 and 10)"
    )
    print("=" * 60)
    print(f"{'Face':<10}{'Frequency':<15}{'Percentage (%)':<15}")
    print("-" * 60)

    # Table data
    for face in range(1, 7):
        print(f"{face:<10}{face_counts[face]:<15}{face_percentages[face]:.2f}%")

    # Total row
    print("-" * 60)
    print(f"{'Total':<10}{total_rolls:<15}{'100.00'}%")
    print("=" * 60)


def main():
    # No fixed random seed - results will be different each time

    # Simulate die rolls
    results = roll_die(1000)

    # Analyze results
    face_counts, face_percentages = analyze_results(results)

    # Print tables
    print_results_table(face_counts, face_percentages, len(results))

    # Also save to file
    original_stdout = sys.stdout
    with open("die_simulation_results.txt", "w") as f:
        sys.stdout = f
        print_results_table(face_counts, face_percentages, len(results))

        sys.stdout = original_stdout

    print("\nResults also saved to die_simulation_results.txt")


if __name__ == "__main__":
    main()
