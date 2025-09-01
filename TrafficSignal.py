def traffic_signal_color(color):
    if color == "red":
        return "Stop"
    elif color == "green":
        return "Go"
    elif color == "yellow":
        return "Caution"
    else:
        return "Invalid color"

signal_color = input("Enter the traffic signal color (red, green, yellow): ").strip().lower()
print(traffic_signal_color(signal_color))