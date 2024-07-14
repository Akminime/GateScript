def run(file):
    """
    This function reads a .gate file and simulates a simple debugging tool for a custom programming language.
    The .gate file contains commands to declare, assign values, and print variables.

    Parameters:
    file (str): The path to the .gate file to be debugged.

    Returns:
    None. The function prints debugging information and errors to the console.
    """
    variables = {}

    if file.endswith(".gate"):
        try:
            with open(file, "r") as f:
                contents = f.readlines()

            for line in contents:
                line = line.strip()

                if line.startswith("var,"):  # Variable declaration
                    try:
                        _, var_def = line.split(" ", 1)
                        var_type, var_name = var_def.split(":")
                        variables[var_name] = {"type": var_type, "value": None}
                        print(f"Variable '{var_name}' of type '{var_type}' declared")
                    except ValueError:
                        raise ValueError(f"Error processing variable declaration line: {line}")

                elif line.startswith("set,"):  # Variable assignment
                    try:
                        _, var_def = line.split(" ", 1)
                        var_name, var_value = var_def.split(":")
                        if var_name in variables:
                            var_type = variables[var_name]["type"]
                            if validate_type(var_type, var_value):
                                variables[var_name]["value"] = var_value
                                print(f"Variable '{var_name}' assigned value '{var_value}'")
                            else:
                                raise TypeError(f"Error: Value '{var_value}' does not match type '{var_type}' for variable '{var_name}'")
                        else:
                            raise NameError(f"Error: Variable '{var_name}' not declared")
                    except ValueError:
                        raise ValueError(f"Error processing variable assignment line: {line}")

                elif line.startswith("prnt,"):  # Print variable value
                    try:
                        _, var_name = line.split(" ", 1)
                        if var_name in variables:
                            print(f"Value of '{var_name}': {variables[var_name]['value']}")
                        else:
                            raise NameError(f"Error: Variable '{var_name}' not declared")
                    except IndexError:
                        raise IndexError(f"Error processing print line: {line}")

                else:
                    raise SyntaxError(f"Unknown command: {line}")

        except (ValueError, TypeError, NameError, IndexError, SyntaxError) as e:
            print(e)
            print("Compilation stopped due to error.")
    else:
        print(f"Invalid file format. Expected '.gate', but got {file.split('.')[-1]}")

def validate_type(var_type, var_value):
    if var_type == "int":
        return var_value.isdigit()
    elif var_type == "str":
        return var_value.startswith('"') and var_value.endswith('"')
    return FalseW