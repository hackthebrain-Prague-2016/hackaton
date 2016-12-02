Creativity Patch

The most puzzling function of the human being is creativity - nobody actually knows what's happening while we are creating something new. That’s why it’s easy to understand that brain mechanisms underlying this process are extremely vague - there is no one clear hypothesis about it. However, after analyzing relevant literature, we’ve chosen one algorithm possibly suitable for the person’s creativity level estimation. We assess creativity in terms of connectivity level (in one of the frequency ranges) between distant cortex regions (e.g. frontal and occipital lobes). Using special math function we estimate synchronicity of waves in such regions. If these waves are synchronised, we propose that these regions are working together providing creativity function for the brain.


How to use this patch?
This patch calculates two substreams (inverse alpha and coherence) that merges to a feature vector. 
You could use this vector as a control parameter; patch sends its to VRPN server (it could be OSC-server).
For this patch you need  the EEG device with electrodes covering the entire head.

Read article, how to use patches in OpenVibe: https://github.com/hackthebrain-Prague-2016/hackaton/blob/master/wiki/How%20to%20use%20patches.md

What’s happening there?

This patch uses some EEG correlates of divergent type of solutions to the problem solving that are part of creative thinking.
Actually, this patch calculates two types of EEG-metrics: magnitude square coherence beetween distant cortex zones 
(you could use either frontopolar-occipital or parietal-temporal) and alpha band power in left hemisphere.

This patch gets data from EEG signal and compares connectivity between two selected channels (using built-in math function - for more information see box documentation). By default it’s frontal and occipital zones but you can choose other variants.  
For more ideas which cortex areas connectivity you can use see this review 
https://www.ncbi.nlm.nih.gov/pubmed/20488210 (full text in the wiki-folder)
