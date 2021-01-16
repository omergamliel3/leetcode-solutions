def validate_perenthesis(string: str) -> bool:
    balance = 0
    for char in string:
        if char == '(':
            balance += 1
        else:
            balance -= 1

    
    return balance == 0


def main():
    result = validate_perenthesis('(())')
    print(result)


if __name__ == "__main__":
    main()
