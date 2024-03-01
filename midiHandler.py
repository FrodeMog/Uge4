import mido
import random

class MidiHandler:
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

    def getNotes(self, file_path, num_notes=5, start_index=0, channel_number=0):
        try:
            mid = mido.MidiFile(file_path)

            if channel_number >= len(mid.tracks):
                raise ValueError("Invalid channel number")

            if not any(msg.type == 'note_on' or msg.type == 'note_off' for msg in mid.tracks[channel_number]):
                raise ValueError(f"No notes found in channel {channel_number}")
            
            # construct a note array: [note, velocity, on_tick, duration]
            # note is the midi note number. 0-127 (88 keys on a piano with odd translation)
            # velocity is the volume of the note. 0-127
            # on_tick is the tick when the note was turned on
            # duration is the number of ticks the note was on for
            notes = []
            note_on_dict = {}
            current_tick = 0
            for msg in mid.tracks[channel_number]:
                current_tick += msg.time
                if msg.type == 'note_on':
                    # Store the note and the tick when it was turned on
                    note_on_dict[msg.note] = [msg.note, msg.velocity, current_tick]
                elif msg.type == 'note_off' and msg.note in note_on_dict:
                    # Calculate the duration
                    duration = current_tick - note_on_dict[msg.note][2]
                    # Append the note, velocity, on_tick and duration to the notes list
                    notes.append(note_on_dict[msg.note] + [duration])
                    # Remove the note from the dictionary
                    del note_on_dict[msg.note]


            # Ensure there are enough notes to select from
            if start_index + num_notes > len(notes):
                raise ValueError("Not enough notes in the MIDI file to select from")

            return notes[start_index : start_index + num_notes]

        except Exception as e:
            #print(f"Error getting notes from MIDI file {file_path}: {e}")
            #return e
            pass

    def getNotesGenerator(self, file_path, num_notes=5, start_index=0, channel_number=0):
        try:
            mid = mido.MidiFile(file_path)

            if channel_number >= len(mid.tracks):
                raise ValueError("Invalid channel number")

            if not any(msg.type == 'note_on' or msg.type == 'note_off' for msg in mid.tracks[channel_number]):
                raise ValueError(f"No notes found in channel {channel_number}")

            # construct a note array: [note, velocity, on_tick, duration]
            # note is the midi note number. 0-127 (88 keys on a piano with odd translation)
            # velocity is the volume of the note. 0-127
            # on_tick is the tick when the note was turned on
            # duration is the number of ticks the note was on for
            notes = []
            note_on_dict = {}
            current_tick = 0
            for msg in mid.tracks[channel_number]:
                current_tick += msg.time
                if msg.type == 'note_on':
                    # Store the note and the tick when it was turned on
                    note_on_dict[msg.note] = [msg.note, msg.velocity, current_tick]
                elif msg.type == 'note_off' and msg.note in note_on_dict:
                    # Calculate the duration
                    duration = current_tick - note_on_dict[msg.note][2]
                    # Append the note, velocity, on_tick and duration to the notes list
                    notes.append(note_on_dict[msg.note] + [duration])
                    # Remove the note from the dictionary
                    del note_on_dict[msg.note]

            # Ensure there are enough notes to select from
            if start_index + num_notes > len(notes):
                raise ValueError("Not enough notes in the MIDI file to select from")

            for note in notes[start_index : start_index + num_notes]:
                yield note

        except Exception as e:
            #print(f"Error getting notes from MIDI file {file_path}: {e}")
            #return e
            pass