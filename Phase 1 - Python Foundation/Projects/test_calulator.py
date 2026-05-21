# test_calculator.py

import pytest

from cli_calculator import CLICalculator


@pytest.fixture
def calculator():
    return CLICalculator()


# -----------------------------
# parse_expression tests
# -----------------------------

def test_parse_addition(calculator):
    num1, operator, num2 = calculator.parse_expression("10 + 20")

    assert num1 == 10.0
    assert operator == "+"
    assert num2 == 20.0


def test_parse_without_spaces(calculator):
    num1, operator, num2 = calculator.parse_expression("10-5")

    assert num1 == 10.0
    assert operator == "-"
    assert num2 == 5.0


def test_parse_decimal_numbers(calculator):
    num1, operator, num2 = calculator.parse_expression("5.5 * 2")

    assert num1 == 5.5
    assert operator == "*"
    assert num2 == 2.0


def test_parse_negative_number(calculator):
    num1, operator, num2 = calculator.parse_expression("-10 + 5")

    assert num1 == -10.0
    assert operator == "+"
    assert num2 == 5.0


def test_parse_invalid_expression(calculator):
    with pytest.raises(ValueError):
        calculator.parse_expression("hello")


# -----------------------------
# calculate tests
# -----------------------------

def test_addition(calculator):
    assert calculator.calculate(10, "+", 20) == 30


def test_subtraction(calculator):
    assert calculator.calculate(10, "-", 5) == 5


def test_multiplication(calculator):
    assert calculator.calculate(5, "*", 4) == 20


def test_division(calculator):
    assert calculator.calculate(10, "/", 2) == 5


def test_modulus(calculator):
    assert calculator.calculate(10, "%", 3) == 1


def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.calculate(10, "/", 0)


def test_modulus_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.calculate(10, "%", 0)


def test_invalid_operator(calculator):
    with pytest.raises(ValueError):
        calculator.calculate(10, "&", 5)


# -----------------------------
# parametrized tests
# -----------------------------

@pytest.mark.parametrize(
    "num1, operator, num2, expected",
    [
        (10, "+", 20, 30),
        (10, "-", 5, 5),
        (5, "*", 4, 20),
        (10, "/", 2, 5),
        (10, "%", 3, 1),
    ],
)
def test_calculate_multiple_cases(
    calculator,
    num1,
    operator,
    num2,
    expected
):
    assert calculator.calculate(num1, operator, num2) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("10 + 20", (10.0, "+", 20.0)),
        ("10-5", (10.0, "-", 5.0)),
        ("5.5 * 2", (5.5, "*", 2.0)),
        ("-10 + 5", (-10.0, "+", 5.0)),
    ],
)
def test_parse_multiple_cases(calculator, expression, expected):
    assert calculator.parse_expression(expression) == expected