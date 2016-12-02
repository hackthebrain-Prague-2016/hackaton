# How to use patch

## So, you have patch for OpenVibe to process data from your device. Proceed with next steps to apply patch.

1. Connect your EEG device to the computer.
1. OpenVibe Acqusition server is a center node, that collects data from devices of different types. Launch OpenVibe Acqusition server and setup it for your EEG device. There could be several ways, that are described below.
1. Launch OpenVibe Designer.
1. Load your patch.
1. There is an inital node "Aquisition client", that will connect to OpenVibe Acqusition server for device data.
1. Wear your EEG device
1. Push “Start” button on the top bar of OpenVibe
1. You can monitor an emotional state in different ways using boxes from “Visualisation” folder from the right column.

## How to set up OpenVibe Acqusition server

1. Launch OpenVibe Acqusition server
1. Choose driver for your device to obtain data from it.
1. Or choose driver for LSLSmartbci (separate program) as another way of recieving data.
1. Press "Connect" for initialising connection to your device
1. Press "Run" to start recieving data

## How to use LSLSmartbci for recieving data

1. Download folder with LSLSmartbci and install it. Download link: https://drive.google.com/drive/folders/0BwlufvWw_B4iLUpoVzlmMlZpUEk?usp=sharing
1. Installation for LSLSmartbci is simple. Install C++ RunTime files by launching vcredist_x64.exe 64 bit Windows or vcredist_x86.exe for 32 bit Windows from the downloaded floder. As C++ RunTime files are installed you could run LSLSmartbci.
1. Launch LSLSmartBCI. There are folders with two versions of LSLSmartbci in the downloaded folder: "LSL(1.0.7918)x64" for 64 bit Windows and "x86" for 32 bit Windows. Choose folder for your Windows and launch LSLSmartBCI.exe inside it.

For the more detailed information on the emotion detection see http://www.sciencedirect.com/science/article/pii/S187704281303646X 
