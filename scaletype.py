from enum import Enum, unique
from note import Intervals

class ScaleType:
    """Representing a scale type. A scale type is basically a building pattern
    for a scale, meaning that it contains all the intervals needed to create a
    certain scale."""
    def __init__(self, name, intervals):
        self.__name = name
        self.__intervals = intervals

    def getIntervals(self):
        """Returns the list of intervals of the scale type."""
        return self.__intervals

    def getName(self):
        """Returns the name of the scale type."""
        return self.__name.name

    def toString(self):
        """Returns a string representation of the scale type."""
        strRep = "ScaleType '" + self.__name.name + "':" "\n"

        for i, interval in enumerate(self.__intervals):
            strRep += interval.name

            if i < (len(self.__intervals) - 1):
                strRep += " "

        return strRep

class ScaleTypeFactory:
    """Factory for creating scale types. Generates an instance of ScaleType
    based on the given ScaleTypeFactory.ScaleTypeName (e.g. Major)."""

    @unique
    class ScaleTypeName(Enum):
        """An enum representing all implemented building patterns of the
        ScaleTypeFactory."""
        Major = 0
        NaturalMinor = 1
        HarmonicMinor = 2
        MelodicMinor = 3

    @staticmethod
    def getScaleType(scaleTypeName):
        """Returns an instance of ScaleType with the intervals according to the
        given scaleTypeName."""
        intervals = []

        if scaleTypeName == ScaleTypeFactory.ScaleTypeName.Major:
            intervals.append(Intervals.Unison)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorSecond)
        elif scaleTypeName == ScaleTypeFactory.ScaleTypeName.NaturalMinor:
            intervals.append(Intervals.Unison)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
        elif scaleTypeName == ScaleTypeFactory.ScaleTypeName.HarmonicMinor:
            intervals.append(Intervals.Unison)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorThird)
        elif scaleTypeName == ScaleTypeFactory.ScaleTypeName.MelodicMinor:
            intervals.append(Intervals.Unison)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MajorSecond)
            intervals.append(Intervals.MinorSecond)
            intervals.append(Intervals.MinorThird)
            intervals.append(Intervals.MinorThird)

        return ScaleType(scaleTypeName, intervals)
