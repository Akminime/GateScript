import argparse
from gatelib import debug, run

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script allows you to compile or run Gate Script files.",
        epilog="For more information, visit the project documentation at https://example.com/docs.",
        usage="python Gate.py {compile, run} file"
    )
    parser.add_argument(
        "function", 
        help="Specify 'compile' to compile the Gate file or 'run' to run it. For example, `Gate compile myfile.gate` or `Gate run myfile.gs`",
        choices=["debug", "run", "compile"]
    )
    parser.add_argument(
        "file", 
        help="The path to the Gate file to be compiled or run. If not in the current directory, supply the full path."
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="GateScript 1.0",
        help="Show the version number of the script."
    )

    args = parser.parse_args()

    if args.function == "compile":
        print("Not implemented yet. Use 'python Gate.py debug myfile.gate' to debug your Gate")
    elif args.function == "run":
        run(args.file)
    elif args.function == "debug":
        debug(args.file)
    else:
        print(f"Invalid function '{args.function}' supplied. Use 'compile' or 'run'.")
