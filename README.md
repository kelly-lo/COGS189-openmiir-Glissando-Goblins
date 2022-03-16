COGS189 OpenMIIR Project - Glissando-Goblins
============================
> Used the [OpenMIRR dataset](https://github.com/sstober/openmiir).

We want to study how brain waves differ between the types of music that participants listen to, specifically to the absence of lyrics in music. We also want to observe if brain waves vary or remain uniform between listening sessions that contain similar types of music. 

### Directory

    .
    ├── ica_data/               # ICA fif files - each file corresponds to one participant, 
    |                           #   generated by Preprocessing.ipynb
    ├── AudioOnsetUtils.py      # helper methods/classes for Preprocessing.ipynb and 
    ├── Classification.ipynb    # classification code (including parsing EEG event data, 
    |                           #   setting up SVM inputs, SVM, checking accuracy)
    ├── Preprocessing.ipynb     # preprocessing code (including dropping bad channels and ICA)
    └── README.md
