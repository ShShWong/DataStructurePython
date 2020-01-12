# Except 的用法
def safeInputAge(prompt):
    inputString = input(prompt)
    try:
        age = int(inputString)
        return age
    except ValueError:
        print("Is not an integer type")
        return safeInputAge(prompt)

if __name__ == "__main__":
    age = safeInputAge("Enter your age:")
    print("Age is",age)