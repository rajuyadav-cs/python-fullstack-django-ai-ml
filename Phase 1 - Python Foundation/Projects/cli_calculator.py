import re


class CLICalculator:

    def __init__(self):
        pass

    def show_menu(self):
        print("""
-------------- CLI CALCULATOR ----------
1 - Calculate
2 - Help
3 - Exit
""")

    def run(self):

        while True:

            self.show_menu()

            choice = input("Enter your choice: ").strip()

            try:

                if choice not in ["1", "2", "3"]:
                    raise ValueError("Enter a valid input")

                if choice == "1":

                    print("Calculation Selected")

                    expression = self.get_expression()

                    num1, operator, num2 = self.parse_expression(
                        expression
                    )

                    result = self.calculate(
                        num1,
                        operator,
                        num2
                    )

                    formatted_result = self.format_result(
                        result
                    )

                    print(
                        f"\nFinal Result: {formatted_result}"
                    )

                elif choice == "2":

                    print("Help Selected")

                    self.show_help()

                elif choice == "3":

                    print("Exiting calculator...")

                    break

            except ValueError as e:

                print(f"\nError: {e}")

    def show_help(self):

        print("""
============== HELP SECTION ==============

This calculator supports basic mathematical operations.

Supported Operators:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus

You can enter expressions in these formats:

10 + 20
10-5
5.5 * 2
100 / 4
20 % 3

Rules:
1. Enter only one operation at a time
2. Spaces are optional
3. Decimal numbers are supported
4. Negative numbers are supported

Invalid Examples:
10 ++ 20
hello
10 &
10 / 0

==========================================
""")

    def get_expression(self):

        return input(
            "\nEnter Expression: "
        ).strip()

    def parse_expression(self, expression):

        pattern = r"(-?\d+(?:\.\d+)?)\s*([+\-*/%])\s*(-?\d+(?:\.\d+)?)"

        match = re.fullmatch(
            pattern,
            expression
        )

        if not match:
            raise ValueError(
                "Invalid expression format"
            )

        num1 = float(match.group(1))

        operator = match.group(2)

        num2 = float(match.group(3))

        return num1, operator, num2

    def calculate(
        self,
        num1,
        operator,
        num2
    ):

        if operator == "+":

            return num1 + num2

        elif operator == "-":

            return num1 - num2

        elif operator == "*":

            return num1 * num2

        elif operator == "/":

            if num2 == 0:
                raise ValueError(
                    "Cannot divide by zero"
                )

            return num1 / num2

        elif operator == "%":

            if num2 == 0:
                raise ValueError(
                    "Cannot use modulus with zero"
                )

            return num1 % num2

        else:

            raise ValueError(
                "Invalid operator"
            )

    def format_result(self, result):

        print("""
Choose Result Format:

1 - Float Result
2 - Integer Result
""")

        choice = input(
            "Enter format choice: "
        ).strip()

        if choice == "1":

            return float(result)

        elif choice == "2":

            return int(result)

        else:

            raise ValueError(
                "Invalid result format choice"
            )


if __name__ == "__main__":

    calculator = CLICalculator()

    calculator.run()