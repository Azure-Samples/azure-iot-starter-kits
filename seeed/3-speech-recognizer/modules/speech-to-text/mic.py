import array
import audioop
import threading

import pocketsphinx as ps
import pyaudio
import RPi.GPIO as GPIO


class MicrophoneThread(threading.Thread):
    SAMPLE_RATE = 44100
    TARGET_RATE = 16000
    CHUNK_SIZE = 8096
    FORMAT = pyaudio.paInt16
    WIDTH = 2
    CHANNELS = 1 # 1 for mono, 2 for stereo, 4 for ReSpeaker quad array
    RESAMPLE_RATIO = float(TARGET_RATE) / float(SAMPLE_RATE)
    BUTTON = 12

    def __init__(self, callback):
        threading.Thread.__init__(self, target=self.run)
        self._stop_event = threading.Event()
        self._callback = callback

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON, GPIO.IN)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        self.stt = ps.Pocketsphinx()

        # Find best audio device to use.
        p = pyaudio.PyAudio()
        audio_device = self.get_audio_device(p)
        print('Using audio device: {}'.format(p.get_device_info_by_index(audio_device)))

        self.mic = p.open(format=self.FORMAT,
                     channels=self.CHANNELS,
                     rate=self.SAMPLE_RATE,
                     frames_per_buffer=self.CHUNK_SIZE,
                     input=True,
                     input_device_index=audio_device)
        self.mic.start_stream()

        self.process_mic(self.mic)        

    def process_mic(self, mic):
        audio_frames = array.array('h')
        while not self.stopped():
            # Capture audio while the button is held.
            if GPIO.input(self.BUTTON):
                if len(audio_frames) == 0:
                    print("Listening ...")

                frames = array.array('h', mic.read(self.CHUNK_SIZE, exception_on_overflow = False))
                audio_frames.extend(frames)

            # The button is not held down, run speech-to-text.
            elif len(audio_frames) > 0:
                print("Processing {} bytes ... ".format(len(audio_frames)))

                # Speech-to-text.
                text = self.speech_to_text(audio_frames)
                print("Heard: {}".format(text))

                # Execute callback.
                try:
                    self._callback(text)
                except Exception as e:
                    print("Exception processing speech-to-text callback: {}".format(e))

                # Reset the captured audio frames.
                audio_frames = array.array('h')

    def speech_to_text(self, audio_frames):
        with self.stt.start_utterance():
            (resampled, _) = audioop.ratecv(audio_frames, self.WIDTH, self.CHANNELS, self.SAMPLE_RATE, self.TARGET_RATE, None)
            self.stt.process_raw(resampled, False, False)
            return self.stt.hypothesis()

    def get_audio_device(self, p):
        index = 0
        for i in range(p.get_device_count()):
            di = p.get_device_info_by_index(i)
            if di['name'].startswith('seeed-4mic-voicecard'):
                return di['index']
            if di['name'] == 'default':
                index = i

        # Return 'default' sound device, if found.
        return index
