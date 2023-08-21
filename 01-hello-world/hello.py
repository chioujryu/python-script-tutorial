import argparse

def main(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say hello to the specified name.')
    parser.add_argument('name', type=str, help='Name to greet')
    args = parser.parse_args()

    main(args.name)
