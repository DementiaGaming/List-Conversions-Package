
def convertToInt(tempList):
    """
    Converts a list of string numbers to a list of integers
    """
    try:
        for i in range(len(tempList)):
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
        for i in range(len(tempList)):
                tempList[i] = str(tempList[i])
        return tempList
    except Exception as e:
        print(f"Error converting list to str: {e}")
        return None
    
def convertToBool(tempList):
    """
    Converts a list of strings with values of either 'True' or 'False' to a list of boolean values
    """
    try:
        for i in range(len(tempList)):
                if tempList[i].lower() == 'true':
                    tempList[i] = True
                elif tempList[i].lower() == 'false':
                    tempList[i] = False
        return tempList
    except Exception as e:
        print(f"Error converting list to bool: {e}")
        return None