from os import path
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
print(model_path)

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm= path.join(model_path, 'es-es/es-es'),
    lm= path.join(model_path, 'es-20k.lm.bin'),
    dict= path.join(model_path, 'es.dict')
)

for phrase in speech:
    print(phrase)