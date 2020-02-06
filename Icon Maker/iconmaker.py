# -*- coding: utf-8 -*-
"""
Eric Metzler
Python 2
Due 2/5/20
Icon Printer

Using loops and a basic data structure, display a 10x10 icon in various scales
and orientation.
"""

def convert(sequence):
    """
    Convert all numbers into different characters.
    """
    convertedList = []
    for number in sequence:
        if number == "1":
            number = "@"
            convertedList.append(number)
        elif number == "0":
            number = " "
            convertedList.append(number)
    return convertedList

def separateToLists(sequence):
    """ 
    This function serves to separate the original string into different
    strings that get dumped back into a list for later printing.
    """
    thebigpicture = []
    count = 0
    pictureList = []
    for number in sequence:
        pictureList.append(number)
        count += 1
        if count == 10:
            pictureLine = "".join(pictureList)
            thebigpicture.append(pictureLine)
            count = 0
            pictureList = []
    return thebigpicture

def hugify(sequence):
    """
    This function will make the picture bigger.  It just appends however many
    times you need it to.  The "scale" variable indicates what dimensions each
    cell will take.  For example, at a scale of 2, each cell becomes a 2x2
    grid.
    """
    thebiggerpicture = []
    scale = 4
    count = 0
    pictureList = []
    for number in sequence:
        for counter in range(scale):
            pictureList.append(number)
        count += 1
        if count == 10:
            pictureLine = "".join(pictureList)
            for counter in range(scale):
                thebiggerpicture.append(pictureLine)
            count = 0
            pictureList = []
    return thebiggerpicture

def inverse(sequence):
    """
    This will take the initial list and assign opposite signs from the convert
    function.
    """
    convertedList = []
    for number in sequence:
        if number == "0":
            number = "@"
            convertedList.append(number)
        elif number == "1":
            number = " "
            convertedList.append(number)
    return convertedList
        

def main():
    pictureSequence = """
    000000000001000011001010011100010011110000000001001111111111
    0000000100000000010000100001000000000000
    """
    initialList = []
    for number in pictureSequence:
        initialList.append(number)
    convertedList = convert(initialList)
    thebigpicture = separateToLists(convertedList)
    for number in thebigpicture:
        print(number)
    thebiggerpicture = hugify(convertedList)
    for number in thebiggerpicture:
        print(number)
    inverseList = inverse(initialList)
    inversePicture = separateToLists(inverseList)
    for number in inversePicture:
        print(number)
    
if __name__ == "__main__":
    main()
