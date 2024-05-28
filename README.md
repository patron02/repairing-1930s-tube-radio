# Repairing my great great grandpa's tube radio

I received the radio in really bad condition because it had been packaged and shipped from Brazil to the USA. The circuit was broken, the wood had termites and was chipped, the fabric was ripped, the speaker was damaged, and the buttons did not work. 

<img src="https://user-images.githubusercontent.com/69320369/212194215-aec0bbb9-9f6e-48b5-8ae7-3b40f1c04e6c.jpg" width="400" />  <img src="https://user-images.githubusercontent.com/69320369/212194839-070d1e12-a39d-41f0-9db2-2f0564185f9c.jpg" width="400" />

The glass on the radio had broken so we got some glass custom made and installed it where the old glass was. We also replaced the torn fabric with some new fabric that we found online. 

I started repairing the circuit by first soldering all the components that had fallen off. I replaced the broken tubes with new ones and fixed the ground connection on the radio. Because the radio was manufactured and used in Brazil it was set to operate at a voltage of 220V. I had to use a voltage converter to switch it to the US standard of 120V. 

https://user-images.githubusercontent.com/69320369/212196168-14f9e4e0-59a8-4e10-b02d-82e086519a75.mp4

<img src="https://user-images.githubusercontent.com/69320369/212196653-a067b2b4-bb27-4873-a10b-dc72b5ffc6ec.jpg" width="400" />

# Installing the bluetooth module

Materials: 
- 12S Class D Amplifier: https://www.adafruit.com/product/3006
- RaspberryPi 3 B+
- 4 GB SD card
- DPDT switch
- micro SD cable
- fan

The rPi does not have amplification from the GPIO pins so the adafruit amplifier module had to be used. GPIO pin 21 will be connected to the DIN on the amplifier. Since there is only one speaker LDR is not necessary. The 5V and GND input will be connected to the corresponding rPi pins. The outputs on the amplifier will be connected to the DPDT switch side 1, the analog radio output will be connected to DPDT side 2, and the speaker input will be connected in the middle of the DPDT switch. 

Setup: 
- install raspbian on the SD card and plug into pi
- connect to network and find IP address
- open rpi terminal and run sudo raspi-config
- on a computer that is on the same network use cmd to run ssh pi@ip-address

Programming: 
- edit config file with IS2 protocol
- sudo systemctl daemon-reload
- sudo systemctl enable bluetooth_audio.service
- sudo systemctl enable fan_control.service





