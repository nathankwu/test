from datetime import date


def calculate_age(birthdate: date, today: date | None = None) -> int:
    if today is None:
        today = date.today()
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1
    return years


def main() -> None:
    while True:
        s = input("Enter your birthday (YYYY-MM-DD): ").strip()
        try:
            bd = date.fromisoformat(s)
            break
        except Exception:
            print("Invalid format. Please use YYYY-MM-DD (e.g. 1990-04-25).")

    age = calculate_age(bd)
    print(f"You are {age} years old.")


if __name__ == "__main__":
    main()
