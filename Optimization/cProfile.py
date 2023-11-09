# Created by Su Myat Phyoe at 08:15 am 27/10/2023 using PyCharm
import profile
import random


def perform_computation(size):
    """A sample function to perform some computation."""
    data = [random.random() for _ in range(size)]
    result = sum(data) / max(data)
    return result


def main():
    """Main function to demonstrate profiling with cProfile."""
    # Use cProfile to profile the perform_computation function

    profile.run('''
for _ in range(1000):
    perform_computation(1000)
''', sort='cumulative')


if __name__ == "__main__":
    main()
