import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python cache_sim.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        k, m = map(int, f.readline().split())
        reqs = list(map(int, f.readline().split()))

    print(f"k={k}, m={m}, requests={reqs}")

main()