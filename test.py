import argparse

if __name__ == '__main__':

    # Initialize the parser
    parser = argparse.ArgumentParser(description="my math script")


    # Add the optional parameters
    parser.add_argument('-n1','--num1', help="Number 1", type=float)
    parser.add_argument('-n2','--num2', help="Number 2", type=float)
    parser.add_argument('-o','--operation', help="provide operator", default='+')


    # Parse the arguments
    args = parser.parse_args()

    result = None
    if args.operation == '+':
        result = args.num1 + args.num2
    if args.operation == '-':
        result = args.num1 - args.num2
    if args.operation == '*':
        result = args.num1 * args.num2
    if args.operation == 'pow':
        result = pow(args.num1, args.num2)

    print("Result : ", result)