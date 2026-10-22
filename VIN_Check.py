# VIN decoder: the user enters a VIN and gets the car's details
 
 
# ---------- Tables ----------
 
# Numeric value of each character (used for the check digit)
values = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "R": 9,
    "S": 2, "T": 3, "U": 4, "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9,
}
 
# Weight of each position in the VIN (17 positions)
weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
 
# Country of manufacture by the first character
countries = {
    "1": "USA", "4": "USA", "5": "USA",
    "2": "Canada", "3": "Mexico",
    "J": "Japan", "K": "Korea / Israel", "L": "China",
    "S": "United Kingdom", "T": "Czech Republic / Switzerland / Hungary",
    "V": "France / Spain", "W": "Germany",
    "Z": "Italy", "Y": "Sweden / Belgium / Finland",
}
 
# Manufacturer by the first three characters (partial list of common makers)
manufacturers = {
    "WVW": "Volkswagen", "WAU": "Audi", "WBA": "BMW", "WDD": "Mercedes-Benz",
    "W0L": "Opel", "TMB": "Skoda", "VSS": "SEAT",
    "VF1": "Renault", "VF3": "Peugeot", "VF7": "Citroën",
    "ZFA": "Fiat", "YV1": "Volvo", "SAL": "Land Rover",
    "JHM": "Honda", "1HG": "Honda", "JN1": "Nissan", "JMZ": "Mazda",
    "JTD": "Toyota", "KMH": "Hyundai", "KNA": "Kia",
    "1FA": "Ford", "1G1": "Chevrolet",
    "5YJ": "Tesla", "LRW": "Tesla", "LSJ": "MG",
}
 
# Year codes: the first code is 1980, the second is 1981, and so on
year_codes = "ABCDEFGHJKLMNPRSTVWXY123456789"
 
 
# ---------- Functions ----------
 
# Check that the VIN is valid: 17 characters, no I, O or Q
def is_valid(vin):
    if len(vin) != 17:
        return False
    for char in vin:
        if char not in values:
            return False
    return True
 
 
# Calculate the check digit (character 9)
def check_digit(vin):
    total = 0
    for i in range(17):
        total = total + values[vin[i]] * weights[i]
    remainder = total % 11
    if remainder == 10:
        return "X"
    return str(remainder)
 
 
# Decode the model year (character 10)
def model_year(vin):
    code = vin[9]
    if code not in year_codes:
        return "Unknown"
    year = 1980 + year_codes.index(code)
    # The codes repeat every 30 years, so pick the later year if possible
    if year + 30 <= 2026:
        year = year + 30
    return year
 
 
# ---------- Main program ----------
 
vin = input("Enter your car's VIN: ").upper().replace(" ", "")
 
if not is_valid(vin):
    print("Invalid VIN: it must be 17 characters, without the letters I, O, Q")
else:
    print()
    print("=== Car details ===")
    print("Country:", countries.get(vin[0], "Unknown"))
    print("Manufacturer:", manufacturers.get(vin[0:3], "Unknown (code " + vin[0:3] + ")"))
    print("Model year:", model_year(vin))
    print("Serial number:", vin[11:17])
    if vin[8] == check_digit(vin):
        print("Check digit: valid")
    else:
        print("Check digit: does not match (common in European cars)")


