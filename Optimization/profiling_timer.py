# Created by Su Myat Phyoe at 10:10 am 19/10/2023 using PyCharm

import random
import time


def perform_computation(size):
    """A sample function to perform some computation."""
    data = [random.random() for _ in range(size)]
    result = sum(data) / max(data)
    return result


def main():
    """Main function to demonstrate timing with a timer."""
    # Record the start time
    start_time = time.time()

    # Call the function multiple times (simulating a workload)
    for _ in range(1000):
        perform_computation(1000)

    # Record the end time
    end_time = time.time()

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
