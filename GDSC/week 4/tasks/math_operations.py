
def basic_operations(a, b):
    try:
        x = a + b
        y = a - b
        z = a * b
        v = a / b

        return {
            "addition": x,
            "subtraction": y,
            "multiplication": z,
            "division": v
        }
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid inputs. Please enter numbers.")

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not valid.")
    except TypeError:
        print("Error: Invalid inputs. Please enter numbers.")

def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except TypeError:
        print("Error: Invalid operation list. Please provide a list of tuples containing a function and its arguments.")