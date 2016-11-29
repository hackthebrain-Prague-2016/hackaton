This patch is an extended version of the Frontal Alpha-asymmetry patch. Here we have a strong additional method helping to discriminate subject’s emotions more accurate. Roughly, this method represents correlation of the EEG features and subject’s emotional state where this state defines as a coordinates on a plane, where we got an arousal on the one axis and a valence on the other. Thus, we consider that every emotion can be represented as a combination of this two components, e.g. fear has a high level of arousal and very negative valence.

For the estimation of the valence the frontal alpha asymmetry was used (see above) and for arousal - values of alpha waves all over the cortex.

How to use this patch?

1. Open OpenVibe.
2. Load “Emotion detection.xml” patch.
3. Connect your (Mitsar) EEG device to the computer.
4. Choose the correct port (xxxx) in your device settings.
5. Wear your EEG device
6. Push “Start” button on the top bar of OpenVibe
7. You can monitor an emotional state in different ways using boxes from “Visualisation” folder from the right column.

**What’s happening there?
This patch gets EEG record or EEG live stream, then chooses a signal only from frontal electrodes (F3 - left, F4 - right), makes filtering leaving only required frequency (in our case it’s alpha waves which are 7-13 Hz). On the next stage the difference in frequency power between left and right is being measured.
Simultaneously the power of alpha waves throughout the cortex is being measured. 
Then the patch uses values from alpha asymmetry for the valence axis coordinate and values from alpha power for the arousal coordinate. So if you have great positive values for both axis it might mean that the subject is extremely happy and vice versa great negative values might show an extremely sad condition of the subject.
Suggestions on this patch. A Dream of many artists fulfills! Now you can create straight from your emotional state avoiding all mental and verbal obstacles. Want to share your emotions with others? Just make up some appropriate image for different emotional states and create some cool transitions. Now let your brain do the rest!

For the more detailed information on the emotion detection see http://www.sciencedirect.com/science/article/pii/S187704281303646X 