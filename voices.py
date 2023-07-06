# Convert the values inside the list to dictionaries then make a list to store all names of voices

voices = [dict(voice_id='21m00Tcm4TlvDq8ikWAM',
              name='Rachel', category='premade',
              description=None, labels=None,
              samples=None,
              settings=dict(stability=0.75, similarity_boost=0.75), design=None),
        dict(voice_id='AZnzlk1XvdvUeBnXmlld', name='Domi', category='premade',
              description=None, labels=None, samples=None,
              settings=dict(stability=0.1, similarity_boost=0.75), design=None),
        dict(voice_id='EXAVITQu4vr4xnSDxMaL', name='Bella', category='premade',
              description=None, labels=None, samples=None,
              settings=dict(stability=0.245, similarity_boost=0.75), design=None),
        dict(voice_id='ErXwobaYiN019PkySvjV', name='Antoni', category='premade',
              description=None, labels=None, samples=None,
              settings=dict(stability=0.195, similarity_boost=0.75), design=None),
        dict(voice_id='MF3mGyEYCl7XYWbV9V6O', name='Elli', category='premade'
              , description=None, labels=None, samples=None,
              settings=dict(stability=0.755, similarity_boost=0.75),
              design=None), dict(voice_id='TxGEqnHWrfWFTfGW9XjX', name='Josh', category='premade',
            description=None, labels=None, samples=None,
                settings=dict(stability=0.15,
                 similarity_boost=0.51), design=None),
        dict(voice_id='VR6AewLTigWG4xSOukaG', name='Arnold',
              category='premade', description=None, labels=None,
              samples=None, settings=dict(stability=0.15,
                                                   similarity_boost=0.75),
              design=None), dict(voice_id='pNInz6obpgDQGcFmaJgB', name='Adam',
                                  category='premade', description=None,
                                  labels=None, samples=None,
                                  settings=dict(stability=0.2, similarity_boost=0.75), design=None),
        dict(voice_id='yoZ06aMxZJJ28mfd3POQ', name='Sam', category='premade',
             description=None, labels=None, samples=None, settings=dict(stability=0.25, similarity_boost=0.75), design=None)]

voices_names = []

for dictionary in voices:
    voices_names.append(dictionary['name'])
print(voices_names)
