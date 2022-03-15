from enum import Enum

participant_list = ["01", "04", "06", "07", "09", "11", "12", "13", "14"] # omit P05

class AudioType(Enum):
    LYRICAL = 0
    NONLYRICAL_LYRICAL = 1
    NON_LYRICAL = 2

id_to_stimuli = {
    0 : 'noise',
    1 : 'Chim Chim Cheree with lyrics',
    2 : 'Take Me Out To The Ballgame with lyrics',
    3 : 'Jingle Bells with lyrics',
    4 : 'Mary Had A Little Lamb with lyrics',
    11 : 'Chim Chim Cheree without lyrics',
    12 : 'Take Me Out To The Ballgame without lyrics',
    13 : 'Jingle Bells without lyrics',
    14 : 'Mary Had A Little Lamb without lyrics',
    21 : 'Emperor Waltz',
    22 : 'Harry Potter Theme',
    23 : 'Star Wars Theme',
    24 : 'Eine kleine Nachtmusik',
}

# Version 1
cue_length_1 = [1.65, 1.867, 2.317, 2.988, 1.669, 1.9, 2.364, 2.975, 1.995, 2.046, 2.307, 3.365]
song_length_1 = [13.3157, 7.6682, 9.6627, 11.6232, 13.8843, 7.9123, 8.9502, 12.2381, 8.3265, 16.0162, 9.2353, 6.8709]

# stimuli_meta1['song_id']['cue_length']
# stimuli_meta1['song_id']['song_length']
# stimuli_meta1['song_id']['audio_type']
stimuli_meta1 = dict()
for idx, key in enumerate(id_to_stimuli):
    if idx == 0: 
        continue
    stimuli_meta1[key] = dict()
    stimuli_meta1[key]['cue_length'] = cue_length_1[idx-1]
    stimuli_meta1[key]['song_length'] = song_length_1[idx-1]
    if 'with lyrics' in id_to_stimuli[key]:
        stimuli_meta1[key]['audio_type'] = AudioType.LYRICAL
    elif 'without lyrics' in id_to_stimuli[key]:
        stimuli_meta1[key]['audio_type'] = AudioType.NONLYRICAL_LYRICAL
    else:
        stimuli_meta1[key]['audio_type'] = AudioType.NON_LYRICAL

# Version 2
cue_length_2 = [1.632, 1.831, 2.317, 2.988, 1.653, 1.869, 2.364, 2.975, 1.995, 2.182, 2.307, 3.365]
song_length_2 = [13.3161, 7.6701, 9.6627, 11.6232, 13.4645, 7.7737, 8.9502, 12.2381, 8.3265, 16.0021, 9.2353, 6.8709]

stimuli_meta2 = dict()
for idx, key in enumerate(id_to_stimuli):
    if idx == 0: 
        continue
    stimuli_meta2[key] = dict()
    stimuli_meta2[key]['cue_length'] = cue_length_2[idx-1]
    stimuli_meta2[key]['song_length'] = song_length_2[idx-1]
    if 'with lyrics' in id_to_stimuli[key]:
        stimuli_meta2[key]['audio_type'] = AudioType.LYRICAL
    elif 'without lyrics' in id_to_stimuli[key]:
        stimuli_meta2[key]['audio_type'] = AudioType.NONLYRICAL_LYRICAL
    else:
        stimuli_meta2[key]['audio_type'] = AudioType.NON_LYRICAL

'''
    Get the stimulus dictionary with format: 

    { version : {
            'song_id' : {
                'cue_length' : Int,
                'song_length' : Int,
                'audio_type' : Int
            }, 
            ...
        }
    }
'''
def get_stim_dict():
    return {
        1: stimuli_meta1,
        2: stimuli_meta2
    }

'''
    Return the dictionary that maps the song ID to song name.
'''
def get_id_to_stim_dict():
    return id_to_stimuli

'''
    Return the song name given song ID.
'''
def get_id_to_song_name(song_id):
    if song_id in id_to_stimuli.keys():
        return id_to_stimuli[song_id]
    else:
        print("song_id does not exist: " + song_id)
        raise ValueError("song_id does not exist")

'''
    Get the list of participants, omitted 5.
'''
def get_participant_list():
    return participant_list


'''
    Get the stimulus version based on participant name.
'''
def get_participant_vers(participant_name):
    vers_1 = ["01", "04", "06", "07"]
    # vers_2 = ["09", "11", "12", "13", "14"]
    if participant_name in participant_list:
        1 if participant_name in vers_1 else 2
    else:
        print("participant_name does not exist: " + participant_name)
        raise ValueError("participant_name does not exist")

'''
    Get the specific dictionary based on version passed in.
'''
def get_vers_stim_dict(vers):
    if vers == 1:
        return stimuli_meta1
    else:
        return stimuli_meta2
