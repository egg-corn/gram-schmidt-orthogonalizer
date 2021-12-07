from sympy import *
import sys
import os


def parse_vector(string):
    """
    parse_vector(string: str) -> tuple(Mul)

    Turns a string representation of a vector to the vector, ie.
    a list of its elements. Uses the sympy 'parse_expr' method.
    Does not support decimals.
    eg. parse_vector('3, 4, 3/6, 1') = (3, 4, 1/2, 1)
    """
    return tuple(map(parse_expr, string.replace(' ', '').split(',')))

opening = """Gram-Schmidt orthogonalizer ver 2.1."""

def clear_screen():
    """
    clear_screen() -> None

    Clears the screen.
    """
    if os.name == 'nt':
        __ = os.system('cls')
    else:
        __ = os.system('clear')
    return

def main():
    """
    main() -> None
    The REPL.
    """

    """
    Part 1: Opening and accepting user input.
    """
    print(opening)
    print()
    print("Start by inputting the number of vectors, eg. 4")

    while True:
        try:
            number_of_vectors = input(">>> ")
            if number_of_vectors == "quit":
                raise SystemExit
            number_of_vectors = int(number_of_vectors)
            assert number_of_vectors > 0
        except SystemExit:
            sys.exit(0)
        except:
            print("Enter a whole number please.")
            continue
        break

    print("Next, enter your vectors one by one, ",
            "seperating entries with commas.")
    print("For example, \"3, 4, 16/5, 3*sqrt(6)/2\" for a 4D vector.")
    print("Do note that decimals (eg. 3.1) are NOT supported.")
    print("Also ensure that your vectors are independent.")
    print("Type 'delete' to remove the previous entry.")
    print()

    list_of_vectors = []
    inputted_vectors = 0
    while inputted_vectors < number_of_vectors:
        if inputted_vectors >= 1:
            print("Keyed-in vectors:")
            for vector in list_of_vectors:
                print(vector)
            print()
        while True:
            try:
                string = input(
                        f"{inputted_vectors}/{number_of_vectors} >>> ")

                if string == "delete":
                    list_of_vectors.pop()
                    inputted_vectors -= 1
                    break
                elif string == "quit":
                    raise SystemExit

                vector = parse_vector(string)
                list_of_vectors.append(vector)
                inputted_vectors += 1
            except SystemExit:
                sys.exit(0)
            except:
                print(("Sorry, we couldn't undersstand what you typed"
                    "Try again."))
                continue
            break
    else:
        v_length = len(list_of_vectors[0])
        if any(len(v) != v_length for v in list_of_vectors):
                print("Your vectors have different lengths. Exiting program.")
                sys.exit(0)

    """
    Part 2: Performing Gram-Schmidt Orthogonalization.
    """


    # All the calculations are done here. The rest is pretty printing.
    old_vectors = list(map(lambda x: Matrix(v_length, 1, x), list_of_vectors))

    try:
        new_vectors = GramSchmidt(old_vectors)
        norms_sq    = [v.norm()**2 for v in new_vectors]
    except ValueError:
        print("Your vectors are not linearly independent. Exiting.")
        sys.exit(0)

    dots = [[v.dot(w) for v in old_vectors] for w in new_vectors]
    normalized_vectors = [v.normalized() for v in new_vectors]
    # End of calculations.
    clear_screen()

    print(f"Let a1, ..., a{number_of_vectors} be the vector(s)",
            f"{str(list_of_vectors)[1:-1]} respectively.")
    print()

    for i in range(number_of_vectors):
        print(f"Step {i}:")
        print()
        if i > 0:
            print("Calculating:")
            print(f"    ||w{i}||^2 = {norms_sq[i-1]}")
            for j in range(i):
                print(f"    a{i+1}.w{j+1}",
                        f"= {tuple(old_vectors[i])}.{tuple(new_vectors[j])}",
                        f"= {dots[j][i]}")
            print()

        define_string = ''.join((f"w{i+1} := a{i+1} ",
            *(f"- (a{i+1}.w{j+1})/(||w{j+1}||^2)*w{j+1} " for j in range(i))))
        working_string = ''.join((f"    = {tuple(old_vectors[i])} ",
            *(f"- ({dots[j][i]})/({norms_sq[j]})*{tuple(new_vectors[i-1])} "
                for j in range(i))))

        print("Define:")
        print(f"    {define_string}")
        print(f"    {working_string}")
        if i > 0:
            print(f"        = {tuple(new_vectors[i])}")
        print()

    else:
        print(f"Step {number_of_vectors}:")
        print()
        print("Calculating:")
        print(f"    ||w{number_of_vectors}||^2 = {norms_sq[-1]}")
        print()
        print("Define:")
        for i in range(number_of_vectors):
            print(f"    v{i+1} := w{i+1}/||w{i+1}||",
                    f"= {tuple(normalized_vectors[i])}")
        print()
        print(f"to obtain a basis T := {{v1, ..., v{number_of_vectors}}}",
                "of orthonormal vectors with the same column space",
                f"as {{a1,...,a{number_of_vectors}}}.")
        print()

if __name__ == "__main__":
    main()
