# ==========================================
# PYTHON EXCEPTION HANDLING - COMPLETE GUIDE
# ==========================================
#
# This file explains:
# 1. try
# 2. except
# 3. else
# 4. finally
# 5. raise
# 6. Custom Exceptions
#
# ------------------------------------------
# WHAT IS EXCEPTION HANDLING?
# ------------------------------------------
#
# Exception handling is used to prevent a
# program from crashing when an error occurs.
#
# Instead of stopping the program,
# Python can handle the error gracefully.
#
# ==========================================


# ==========================================
# 1. BASIC EXCEPTION EXAMPLE
# ==========================================

print("\n--- Example 1: Basic Exception ---")

try:
    # Risky code
    result = 10 / 0

except:
    # Runs if error occurs
    print("An error occurred")

print("Program continues")


# ==========================================
# 2. SPECIFIC EXCEPTION HANDLING
# ==========================================

print("\n--- Example 2: Specific Exception ---")

try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")


# ==========================================
# 3. HANDLING MULTIPLE EXCEPTIONS
# ==========================================

print("\n--- Example 3: Multiple Exceptions ---")

try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# ==========================================
# 4. USING 'as' TO STORE ERROR MESSAGE
# ==========================================

print("\n--- Example 4: Exception Object ---")

try:
    x = 10 / 0

except ZeroDivisionError as error:
    print("Error message:", error)


# ==========================================
# 5. ELSE BLOCK
# ==========================================
#
# else runs only if NO exception occurs.
#
# ==========================================

print("\n--- Example 5: else Block ---")

try:
    value = 10 / 2

except ZeroDivisionError:
    print("Cannot divide")

else:
    print("Division successful")


# ==========================================
# 6. FINALLY BLOCK
# ==========================================
#
# finally ALWAYS runs.
#
# Used for:
# - Closing files
# - Closing database connections
# - Cleanup tasks
#
# ==========================================

print("\n--- Example 6: finally Block ---")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Division error")

finally:
    print("This always executes")


# ==========================================
# 7. FILE HANDLING WITH FINALLY
# ==========================================

print("\n--- Example 7: File Handling ---")

file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
        print("File closed")


# ==========================================
# 8. RAISING EXCEPTIONS MANUALLY
# ==========================================
#
# raise is used to create an exception manually.
#
# ==========================================

print("\n--- Example 8: raise Keyword ---")

age = -5

try:

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as error:
    print(error)


# ==========================================
# 9. PASSWORD VALIDATION EXAMPLE
# ==========================================

print("\n--- Example 9: Password Validation ---")

password = "123"

try:

    if len(password) < 6:
        raise ValueError(
            "Password must contain at least 6 characters"
        )

except ValueError as error:
    print(error)


# ==========================================
# 10. CUSTOM EXCEPTION
# ==========================================
#
# We can create our own exceptions.
#
# Syntax:
#
# class MyError(Exception):
#     pass
#
# ==========================================

print("\n--- Example 10: Custom Exception ---")


class InsufficientBalanceError(Exception):
    """
    Custom exception for low account balance
    """
    pass


# ==========================================
# 11. USING CUSTOM EXCEPTION
# ==========================================

def withdraw(balance, amount):

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    return balance - amount


try:

    remaining_balance = withdraw(1000, 2000)

    print("Remaining:", remaining_balance)

except InsufficientBalanceError as error:

    print("Custom Exception:", error)


# ==========================================
# 12. MULTIPLE EXCEPTIONS IN ONE BLOCK
# ==========================================

print("\n--- Example 12: Multiple Exceptions Together ---")

try:

    value = int("abc")

except (ValueError, TypeError):

    print("Either ValueError or TypeError occurred")


# ==========================================
# 13. NESTED TRY-EXCEPT
# ==========================================

print("\n--- Example 13: Nested try-except ---")

try:

    print("Outer try block")

    try:
        result = 10 / 0

    except ZeroDivisionError:
        print("Inner exception handled")

except:
    print("Outer exception handled")


# ==========================================
# 14. GENERIC EXCEPTION HANDLER
# ==========================================
#
# Exception catches almost all exceptions.
#
# ==========================================

print("\n--- Example 14: Generic Exception ---")

try:

    data = [1, 2, 3]

    print(data[10])

except Exception as error:

    print("Error:", error)


# ==========================================
# 15. USER-DEFINED VALIDATION EXAMPLE
# ==========================================

print("\n--- Example 15: Age Validation ---")


class InvalidAgeError(Exception):
    pass


def check_age(age):

    if age < 18:
        raise InvalidAgeError(
            "Age must be 18 or above"
        )

    return "Eligible"


try:

    print(check_age(15))

except InvalidAgeError as error:

    print(error)

finally:

    print("Validation completed")


# ==========================================
# IMPORTANT NOTES
# ==========================================
#
# try:
#     Risky code
#
# except:
#     Runs if error occurs
#
# else:
#     Runs if NO error occurs
#
# finally:
#     Always runs
#
# raise:
#     Used to manually create exceptions
#
# Custom Exceptions:
#     Used for project/business-specific errors
#
# ==========================================


# ==========================================
# BEST PRACTICES
# ==========================================
#
# 1. Catch specific exceptions whenever possible
#
# GOOD:
# except ValueError:
#
# BAD:
# except:
#
#
# 2. Use finally for cleanup
#
#
# 3. Use meaningful custom exception names
#
#
# 4. Never silently ignore exceptions
#
# BAD:
# except:
#     pass
#
# ==========================================


# ==========================================
# END OF FILE
# ==========================================