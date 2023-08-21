import argparse

def main(name, count, uppercase):
    message = f"Hello, {name}!"
    if uppercase:
        message = message.upper()
    for _ in range(count):
        print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say hello to the specified name.')
    parser.add_argument('name', type=str, required=True, help='Name to greet')
    parser.add_argument('-c', '--count', type=int, default=1, required=True, help='Number of times to greet')
    parser.add_argument('--uppercase', action='store_true', required=False, help='Output greeting in uppercase')
    args = parser.parse_args()

    main(args.name, args.count, args.uppercase)