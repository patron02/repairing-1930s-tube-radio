#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set GPIO pin for the fan
FAN_PIN = 18

# Set the temperature threshold (in Celsius) to turn the fan on
TEMP_THRESHOLD = 50

def setup_gpio():
    # Set GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    # Set the fan pin as output
    GPIO.setup(FAN_PIN, GPIO.OUT)

def get_cpu_temperature():
    # Read CPU temperature from the system file
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = float(f.read()) / 1000.0
    return temp

def control_fan():
    while True:
        # Get the current CPU temperature
        cpu_temp = get_cpu_temperature()

        # If CPU temperature exceeds the threshold, turn the fan on
        if cpu_temp > TEMP_THRESHOLD:
            GPIO.output(FAN_PIN, GPIO.HIGH)
            print(f"Fan turned on. CPU temperature: {cpu_temp:.1f}°C")
        # Otherwise, turn the fan off
        else:
            GPIO.output(FAN_PIN, GPIO.LOW)
            print(f"Fan turned off. CPU temperature: {cpu_temp:.1f}°C")

        # Wait for a few seconds before checking the temperature again
        time.sleep(5)

def cleanup():
    # Clean up GPIO settings
    GPIO.cleanup()

def main():
    try:
        print("Fan control script started. Press Ctrl+C to exit.")
        setup_gpio()
        control_fan()
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        cleanup()

if __name__ == "__main__":
    main()
