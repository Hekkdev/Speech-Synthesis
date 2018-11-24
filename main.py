from flask import make_response
import synthesizer as synth


def synthesize_speech(request):
    request_json = request.get_json(silent=True)

    text = request_json['text']

    s = synth.Synthesizer()
    s.load("./nawar-trained-model/model.ckpt-200000")

    response = make_response(s.synthesize(text))

    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=speech.wav'

    return response
