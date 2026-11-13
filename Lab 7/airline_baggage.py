import math

def parse_booking(code):
    if not isinstance(code, str):
        return None
    parts = code.strip().split('-')
    if len(parts) != 3:
        return None
    airline, flight_str, seat = parts
    airline = airline.strip()
    seat = seat.strip()
    if not airline or not seat:
        return None
    try:
        flight_num = int(flight_str.strip())
    except ValueError:
        return None
    return airline.upper(), flight_num, seat[-1].upper()

def total_weight(weights_csv):
    if not isinstance(weights_csv, str):
        return 0.0
    total = 0.0
    for w in weights_csv.split(','):
        w = w.strip()
        if not w:
            continue
        try:
            val = float(w)
            if not math.isnan(val) and not math.isinf(val) and val >= 0:
                total += val
        except ValueError:
            continue
    return round(total, 2)

def tag_label(name):
    if not isinstance(name, str):
        return ""
    parts = name.strip().split()
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0].upper()
    return parts[0][0].upper() + '. ' + parts[-1].upper()

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)

if __name__ == "__main__":
    main()
