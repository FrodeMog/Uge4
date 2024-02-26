import mido

class GeneratorReadMidi:
    def __init__(self):
        pass

    # Read using regular return
    def readMidi(self, file_path):
        try:
            mid = mido.MidiFile(file_path)
            return list(mid)
        except FileNotFoundError as e:
            print(f"Error reading MIDI file {file_path}: {e}")
            return None
        except Exception as e:
            return e
        
    # Read using generator yield
    def readMidiGenerator(self, file_path):
        try:
            mid = mido.MidiFile(file_path)
            for item in mid:
                yield item
        except FileNotFoundError as e:
            print(f"Error reading MIDI file {file_path}: {e}")
            return None
        except Exception as e:
            return e