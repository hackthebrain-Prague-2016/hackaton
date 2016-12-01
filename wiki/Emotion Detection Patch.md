This patch is an extended version of the Frontal Alpha-asymmetry patch. Here we have a strong additional method helping to discriminate subject’s emotions more accurate. Roughly, this method represents correlation of the EEG features and subject’s emotional state where this state defines as a coordinates on a plane, where we got an arousal on the one axis and a valence on the other. Thus, we consider that every emotion can be represented as a combination of this two components, e.g. fear has a high level of arousal and very negative valence.

For the estimation of the valence the frontal alpha asymmetry was used (see above) and for arousal - values of alpha waves all over the cortex.

How to use this patch?

1. Connect your EEG device to the computer.
1. OpenVibe Acqusition server is a center node, that collects data from devices of different types. Launch OpenVibe Acqusition server and setup it for your EEG device. There could be several ways, that are described below.
1. Launch OpenVibe Designer.
1. Load “Emotion detection.xml” patch.
1. There is an inital node "Aquisition client", that will connect to OpenVibe Acqusition server for device data.
1. Wear your EEG device
1. Push “Start” button on the top bar of OpenVibe
1. You can monitor an emotional state in different ways using boxes from “Visualisation” folder from the right column.

How to set up OpenVibe Acqusition server

1. Launch OpenVibe Acqusition server
1. Choose driver for your device to obtain data from it.
1. Or choose driver for LSLSmartbci (separate program) as another way of recieving data.
1. Press "Connect" for initialising connection to your device
1. Press "Run" to start recieving data

How to use LSLSmartbci for recieving data

1. Download folder with LSLSmartbci and install it. Download link: https://drive.google.com/drive/folders/0BwlufvWw_B4iLUpoVzlmMlZpUEk?usp=sharing
1. Installation for LSLSmartbci is simple. Install C++ RunTime files by launching vcredist_x64.exe 64 bit Windows or vcredist_x86.exe for 32 bit Windows from the downloaded floder. As C++ RunTime files are installed you could run LSLSmartbci.
1. Launch LSLSmartBCI. There are folders with two versions of LSLSmartbci in the downloaded folder: "LSL(1.0.7918)x64" for 64 bit Windows and "x86" for 32 bit Windows. Choose folder for your Windows and launch LSLSmartBCI.exe inside it.

**What’s happening there?
This patch gets EEG record or EEG live stream, then chooses a signal only from frontal electrodes (F3 - left, F4 - right), makes filtering leaving only required frequency (in our case it’s alpha waves which are 7-13 Hz). On the next stage the difference in frequency power between left and right is being measured.
Simultaneously the power of alpha waves throughout the cortex is being measured. 
Then the patch uses values from alpha asymmetry for the valence axis coordinate and values from alpha power for the arousal coordinate. So if you have great positive values for both axis it might mean that the subject is extremely happy and vice versa great negative values might show an extremely sad condition of the subject.
Suggestions on this patch. A Dream of many artists fulfills! Now you can create straight from your emotional state avoiding all mental and verbal obstacles. Want to share your emotions with others? Just make up some appropriate image for different emotional states and create some cool transitions. Now let your brain do the rest!

For the more detailed information on the emotion detection see http://www.sciencedirect.com/science/article/pii/S187704281303646X 
