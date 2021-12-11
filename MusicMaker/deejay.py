from pydub import AudioSegment

melody = AudioSegment.from_wav(r"C:\Users\Pau Sevilla Guill\Documents\GITHUB REPOS\MusicMaker\SFX\House Drop Synth Loop.wav")
base = AudioSegment.from_wav(r"C:\Users\Pau Sevilla Guill\Documents\GITHUB REPOS\MusicMaker\SFX\House Drum Loop 128.wav")

mix = base.overlay(melody, position=1)

mix.export("DJ_RocketSample.mp3", format="mp3")