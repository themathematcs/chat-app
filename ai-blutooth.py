import bluetooth

def turn_on_bluetooth():
    """Turn on Bluetooth on the computer."""
    bluetooth.enable()

def turn_off_bluetooth():
    """Turn off Bluetooth on the computer."""
    bluetooth.disable()

state = input("usage: turn on or off")
# Example usage
if state == "on" or state == "ON" or state == "On" or state == "nO":
    turn_on_bluetooth()
# Wait a few seconds for Bluetooth to turn on...
elif state == "off": 
    turn_off_bluetooth()

