import os
import time
from gpiozero import PWMOutputDevice

# Define GPIO Pin for Audio Output
AUDIO_PIN = 21

# Create PWM Output Device for Audio
audio_output = PWMOutputDevice(AUDIO_PIN)

def setup_bluetooth_audio():
    # Install and start PulseAudio if not already installed
    os.system("sudo apt-get install pulseaudio pulseaudio-module-bluetooth")
    time.sleep(1)
    os.system("pulseaudio --start")
    time.sleep(1)
    os.system("pacmd load-module module-bluetooth-discover")

    # Make Raspberry Pi discoverable via Bluetooth
    os.system("sudo bluetoothctl discoverable on")

def main():
    print("Setting up Bluetooth audio and making Raspberry Pi discoverable...")
    setup_bluetooth_audio()

    try:
        while True:
            # Set audio output to 50% (0.5 duty cycle) for demonstration
            audio_output.value = 0.5
            time.sleep(1)  # Adjust as needed
    except KeyboardInterrupt:
        pass  # Do nothing when Ctrl+C is pressed

if __name__ == "__main__":
    main()
