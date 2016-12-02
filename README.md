# Hackaton

Here we present patches which you can use as a preset for your work on this Hackathon. All patches are created in OpenVibe with some additional python scripts. OpenVibe is an open source software for BCI and online EEG processing. Since it is open source you are free to make any changes and upgrades both in the code or/and in the structure of the patches. Information, download files and tutorials on OpenVibe you will find here http://openvibe.inria.fr/. For use these patches (as well as for use any hardware and software for BCI) you ought to know some basic things about EEG. Electroencephalography (EEG) is an electrophysiological monitoring method to record electrical activity of the brain. The source of this activity is synchronous work of millions neurons in the brain cortex. Each area of the cortes is considered to response for it’s own function, that’s why it is very important to place electrodes on their right position. Most of people working with EEG use 10-20 international system for EEG electrodes placement. More detailed you can read about it here https://en.wikipedia.org/wiki/10-20_system_(EEG). Although commercial EEG devices (such as Muse, Emotive etc.) don’t allow you to place electrodes as accurate as professional ones do, you still have to mind the position of your device on the subject’s head.

How to connect your device to Openvibe?

Connect your EEG device to the computer.
OpenVibe Acqusition server is a center node, that collects data from devices of different types. Launch OpenVibe Acqusition server and setup it for your EEG device. There could be several ways, that are described below.
Launch OpenVibe Designer.
Load “Creativity.xml” patch.
There is an inital node "Aquisition client", that will connect to OpenVibe Acqusition server for device data.
Wear your EEG device
Push “Start” button on the top bar of OpenVibe
You can monitor an emotional state in different ways using boxes from “Visualisation” folder from the right column.
How to set up OpenVibe Acqusition server

Launch OpenVibe Acqusition server
Choose driver for your device to obtain data from it.
Or choose driver for LSLSmartbci (separate program) as another way of recieving data.
Press "Connect" for initialising connection to your device
Press "Run" to start recieving data
How to use LSLSmartbci for recieving data

Download folder with LSLSmartbci and install it. Download link: https://drive.google.com/drive/folders/0BwlufvWw_B4iLUpoVzlmMlZpUEk?usp=sharing
Installation for LSLSmartbci is simple. Install C++ RunTime files by launching vcredist_x64.exe 64 bit Windows or vcredist_x86.exe for 32 bit Windows from the downloaded floder. 
As C++ RunTime files are installed you could run LSLSmartbci.
Launch LSLSmartBCI. There are folders with two versions of LSLSmartbci in the downloaded folder: "LSL(1.0.7918)x64" for 64 bit Windows and "x86" for 32 bit Windows. 
Choose folder for your Windows and launch LSLSmartBCI.exe inside it.



In the wiki folder you will find short description on every patches we provide here. Good luck!
