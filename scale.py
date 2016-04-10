from enum import IntEnum
from note import Note, Intervals
from scaletype import ScaleType, ScaleTypeFactory
import pdb

class Scale:
    """Representation of a musical scale. Based on a root note and a scale type."""
    __notes = []
    __intervals = []

    def __init__(self, root, scaleTypeName):
        self.__root = root
        self.__scaleTypeName = scaleTypeName
        self.__scaleType = ScaleTypeFactory.getScaleType(scaleTypeName)
        self.__generate()

    def __generate(self):
        """Generates the notes of the scale based on scale type and.__root note."""
        self.__intervals = self.__scaleType.getIntervals()
        lastNote = self.__root

        for interval in self.__intervals:
            lastNote = lastNote.getInterval(interval)
            self.__notes.append(lastNote)

    def getNotes(self):
        """Returns the notes of the scale as a list."""
        return self.__notes

    def toString(self):
        """Returns a string representation of the scale."""
        strRep = self.__root.getName().name + " " + self.__scaleTypeName.name + ":\n"
        strRep += "["

        for i, note in enumerate(self.__notes):
            strRep += note.getName().name

            if i < len(self.__notes) - 1:
                strRep += ","

        strRep += "]"

        return strRep
