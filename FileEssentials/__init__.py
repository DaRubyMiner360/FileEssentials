import os

os.system("")

# Creates a file
def CreateFile(name, ifexists = False):
    name = str(name)

    f = None
    if ifexists:
        if not os.path.exists(name):
            f = open(name, 'x')
    else:
        f = open(name, 'x')
    return f
    
# Deletes a file
def DeleteFile(name):
    name = str(name)

    # os.remove(name)
    if os.path.exists(name):
        os.remove(name)
    else:
        print("\033[91m" + "The file does not exist" + "\033[0m")

# Deletes a directory
def DeleteDirectory(name):
    name = str(name)

    # os.rmdir(name)
    if os.path.exists(name):
        os.rmdir(name)
    else:
        print("\033[91m" + "The directory does not exist" + "\033[0m")

# Reads a file
def ReadFile(name):
    name = str(name)

    f = open(name, 'r')
    contents = f.read()
    return contents

# Reads a file's lines
def ReadFileLines(name):
    name = str(name)

    f = open(name, 'r')
    contents = f.readlines()
    return contents
    
# Reads a line of a file
def ReadFileLine(name, line):
    name = str(name)
    line = int(line)

    f = open(name, 'r')
    lines = f.readlines()
    line = lines[line - 1]
    return line
    
# Writes to a file
def WriteFile(name, text):
    name = str(name)
    text = str(text)

    f = open(name, 'w')
    f.write(text)
    return f

# Appends text to a file
def AppendFile(name, text):
    name = str(name)
    text = str(text)

    f = open(name, 'a')
    f.write(text)
    return f

# Checks if a file exists
def CheckFileExists(name):
    name = str(name)

    exists = os.path.exists(name)
    return exists

# Creates a file
def Create(name, ifexists = False):
    return CreateFile(name, ifexists)

# Deletes a file
def Delete(name):
    DeleteFile(name)

# Deletes a directory
def DeleteDir(name):
    DeleteDirectory(name)

# Reads a file    
def Read(name):
    return ReadFile(name)

# Reads a file's lines
def ReadLines(name):
    return ReadFileLines(name)

# Reads a line of a file
def ReadLine(name, line):
    return ReadFileLine(name, line)

# Writes to a file
def Write(name, text):
    return WriteFile(name, text)

# Appends text to a file    
def Append(name, text):
    return AppendFile(name, text)

# Checks if a file exist    
def CheckExists(name):
    return CheckFileExists(name)
    