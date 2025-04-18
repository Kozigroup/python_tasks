def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def main():
    # Test cases
    print("Case 1 (weekday=False, vacation=False):", sleep_in(False, False))  # True
    print("Case 2 (weekday=True, vacation=False):", sleep_in(True, False))   # False
    print("Case 3 (weekday=False, vacation=True):", sleep_in(False, True))   # True


if __name__ == "__main__":
    main()