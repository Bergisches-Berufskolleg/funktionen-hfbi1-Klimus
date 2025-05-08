
def isLeapYear(year):
    # Prüft, ob ein Jahr ein Schaltjahr ist
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = 2025
    result = isLeapYear(year)
    print(f"{year} ist {'ein Schaltjahr' if result else 'kein Schaltjahr'}")
    
if __name__ == "__main__":
    main()
