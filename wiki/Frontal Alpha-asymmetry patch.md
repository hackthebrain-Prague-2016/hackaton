Alpha waves are neural oscillations in the frequency range from 7 to 13 Hz. Difference in alpha power between frontal lobes is considered to reference emotions that the person experiences at the present moment. Roughly, if the power of alpha waves is greater on the right side, it means that he/she feels positive emotions, vice versa - negative emotions.
Why so? It’s believed that right and left frontal lobes play different roles in production of emotions in human. Activity in the right lobe is considered to correlate with negative emotions (more precisely - with avoidance motivation) , in the left lobe - positive (more precisely - with approach motivation). The greater alpha waves are the lower level of activation of given cortex structure is, thus, if we measure greater alpha activity, for example, on the right side in comparison with the left side, we can say that left side is more active and the subject, probably, experiences positive emotions.
How to use this patch?

Connect your EEG device to the computer.
OpenVibe Acqusition server is a center node, that collects data from devices of different types. Launch OpenVibe Acqusition server and setup it for your EEG device. There could be several ways, that are described below.
Launch OpenVibe Designer.
Load “Emotion detection.xml” patch.
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
Installation for LSLSmartbci is simple. Install C++ RunTime files by launching vcredist_x64.exe 64 bit Windows or vcredist_x86.exe for 32 bit Windows from the downloaded floder. As C++ RunTime files are installed you could run LSLSmartbci.
Launch LSLSmartBCI. There are folders with two versions of LSLSmartbci in the downloaded folder: "LSL(1.0.7918)x64" for 64 bit Windows and "x86" for 32 bit Windows. Choose folder for your Windows and launch LSLSmartBCI.exe inside it.

What’s happening there?
This patch gets EEG record or EEG live stream, then chooses a signal only from frontal electrodes (F3 - left, F4 - right), makes filtering leaving only required frequency (in our case it’s alpha waves which are 7-13 Hz). On the next stage the difference in frequency power between left and right is being measured and the program displays the result as intensity of red color. The greater this difference is the more saturated color we can see.
Suggestions on this patch. Information you can get from this patch is very useful for neuroart, because, potentially, it gives you an access to the one of the most important features of the mental state - dominance motivation and consequential gives you a possibility to generate any pieces of art (music, pictures etc.) in correspondence with subject’s unconscious motivation dominance.


For the more detailed information on the frontal alpha asymmetry see http://www.sciencedirect.com/science/article/pii/S0301051109001823 
