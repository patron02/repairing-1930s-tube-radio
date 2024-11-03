# Repairing my great great grandpa's tube radio

The end goal for this project is to repair the radio so that it is functional while keeping the original aesthetic. I will be implementing a bluetooth module in the radio as well so that it is more practical to use. 

I received the radio in really bad condition because it had been packaged and shipped from Brazil to the USA. The circuit was broken, the wood had termites and was chipped, the speaker was damaged, and the knobs did not work. The first step was removing the termites and repairing the wood. 

<img src="https://user-images.githubusercontent.com/69320369/212194215-aec0bbb9-9f6e-48b5-8ae7-3b40f1c04e6c.jpg" height="300" />  <img src="https://user-images.githubusercontent.com/69320369/212194839-070d1e12-a39d-41f0-9db2-2f0564185f9c.jpg" height="300" /> <img src="https://user-images.githubusercontent.com/69320369/212196653-a067b2b4-bb27-4873-a10b-dc72b5ffc6ec.jpg" height="300" />

The glass on the radio had broken so we got some glass custom made and also replaced the fabric. 

# Installing the bluetooth module

Materials: 
- 12S Class D Amplifier: https://www.adafruit.com/product/3006
- RaspberryPi 3 B+
- 32 GB SD card
- DPDT switch
- micro SD cable
- fan

The rPi does not have amplification from the GPIO pins so the adafruit amplifier module had to be used. GPIO pin 21 will be connected to the DIN on the amplifier. Since there is only one speaker LDR is not necessary. The 5V and GND input will be connected to the corresponding rPi pins. The outputs on the amplifier will be connected to the DPDT switch side 1, the analog radio output will be connected to DPDT side 2, and the speaker input will be connected in the middle of the DPDT switch. 

Setup: 
- install raspbian on the SD card and plug into pi
- connect to network and find IP address
- use this tutorial to install bluetooth: https://www.instructables.com/Raspberry-Pi-Bluetooth-Speaker/

Programming: 
Many additional things had to be added to the bluetooth
- installing all new updates packages for bluealsa
- implementing bluetooth so it is not applicable for only 1 device
- amplification

<img src="https://github.com/user-attachments/assets/56819aab-b060-4d77-865c-5a99c160e49c" height="300" />


# Circuit Repair 
Original Circuit: <br>
<img src="https://github.com/user-attachments/assets/5833c737-99a5-4d7e-b264-ce57337919d8" height="500" />




