from enum import Enum, IntEnum, unique

class Intervals(IntEnum):
    """Intervals matched to halftone steps with long names (e.g. MinorSecond) and
    short names (e.g. m2)."""
    Unison = 0
    MinorSecond = 1
    MajorSecond = 2
    MinorThird = 3
    MajorThird = 4
    Fourth = 5
    Tritone = 6
    Fifth = 7
    MinorSixth = 8
    MajorSixth = 9
    MinorSeventh = 10
    MajorSeventh = 11
    Octave = 12

    P1 = 0
    m2 = 1
    M2 = 2
    m3 = 3
    M3 = 4
    P4 = 5
    d5 = 6
    A4 = 6
    P5 = 7
    m6 = 8
    M6 = 9
    m7 = 10
    M7 = 11
    P8 = 12

@unique
class Velocity(IntEnum):
    """Velocities divided into 5 categories."""
    hard = 100
    normal = 75
    soft = 50
    extrasoft = 25
    silent = 0

@unique
class NoteLength(Enum):
    """Representation of note lengths matched to floats."""
    whole = 1
    half = 0.5
    quarter = 0.25
    eigth = 0.125
    sixteenth = 0.0625
    thirtysecond = 0.03125

@unique
class NoteNames(IntEnum):
    """Assigns numbers to all 12 notes, starting with A at 0"""
    A   = 0
    Bb  = 1
    B   = 2
    C   = 3
    Db  = 4
    D   = 5
    Eb  = 6
    E   = 7
    F   = 8
    Gb  = 9
    G   = 10
    Ab  = 11

class Note:
    """Represents a single pitch with certain pitch, velocity and length.
    Specific notes can be created with NoteFactory and NoteNames"""
    def __init__(self, name, pitch, velocity, length):
        self.__name = name
        self.pitch = pitch
        self.velocity = velocity
        self.length = length

    def getName(self):
        """Returns the name of the note."""
        return self.__name

    def getVelocity(self):
        """Returns the velocity of the note."""
        return self.velocity

    def getPitch(self):
        """Returns the MIDI pitch of the note."""
        return self.pitch

    def getLength(self):
        """Returns the length of the note as a value of NoteLength."""
        return self.length

    def getInterval(self, interval, goUp = True):
        """Gets the given interval of the note. goUp specifies wether the interval
        should go to corresponding higher note or to the corresponding lower note
        (if goUp = false)."""
        return NoteFactory.getInterval(self, interval, goUp)

class NoteFactory:
    """Creates MIDI notes based on given NoteName, octave and optionally velocity
    and/or length."""
    __MIDI_MIN_PITCH = 21
    __MIDI_MAX_PITCH = 108
    __OCTAVE_TONES = 12
    __MAX_VELOCITY = 100

    def getNote(noteName, octave, velocity=__MAX_VELOCITY, length=NoteLength.quarter):
        """Creates a new Note instance with given noteName, octave, velocity (optional)
        and length(optional). If velocity is not specified it is set to 100, if
        length is not specified it is set to NoteLength.quarter"""
        return Note(noteName, NoteFactory.__calcPitch(noteName, octave), velocity, length)

    def getInterval(note, interval, goUp = True):
        """Gets the given interval of the note. goUp specifies wether the interval
        should go to corresponding higher note or to the corresponding lower note
        (if goUp = false)."""
        newPitch = note.getPitch()
        newName = note.getName()
        notes = list(NoteNames)

        if goUp:
            newPitch += interval
            newName = notes[(notes.index(newName)+interval) % len(notes)]
        else:
            newPitch -= interval
            newName = notes[(notes.index(newName)-interval) % len(notes)]

        if newPitch <= NoteFactory.__MIDI_MAX_PITCH and newPitch >= NoteFactory.__MIDI_MIN_PITCH:
            return Note(newName, newPitch, note.getVelocity(), note.getLength())
        else:
            return note

    def __calcPitch(note, octave):
        """Calculates the MIDI pitch of a note."""
        return NoteFactory.__MIDI_MIN_PITCH + octave * NoteFactory.__OCTAVE_TONES + note

