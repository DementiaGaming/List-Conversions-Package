
def convertToInt(tempList):
    """
    Converts a list of string numbers to a list of integers
    """
    try:
        for i in range(tempList):
                tempList[i] = int(tempList[i])
        return tempList
    except Exception as e:
        print(f"Error converting list to int: {e}")
        return None
    
def convertToStr(tempList):
    """
    Converts a list of integers to a list of strings
    """
    try:
        for i in range(tempList):
                tempList[i] = str(tempList[i])
        return tempList
    except Exception as e:
        print(f"Error converting list to str: {e}")
        return None