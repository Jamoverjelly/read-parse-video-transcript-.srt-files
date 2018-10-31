import re
import os
from fnmatch import fnmatch

# update python's location to transcript directory using path address
os.chdir('DIRECTORY-PATH-OF-TRANSCRIPT-FILES-TO-PROCESS/')
# Update the above string passed to os.chdir to full path of folder containing
# all folders of .srt files you intend to process.
# Example: '/Users/YOUR-HOME-DIRECTORY/Downloads/Trascript-Folders-to-Parse/'

# get string of current directory and assign into variable
parentDir = os.getcwd()

# empty list object created for holding each directory string
directoryList = []

# empty list object created for holding each english .srt file string
englishSrtFiles = []

# empty list object created for holding each file string prepared for processing
fileNameList = []


def createDirectoryList():
    # DEFINITION:
    # This function creates a directory listing as a collection of strings
    # from the given parent directory and then qualifies each string to check
    # if it is in fact a directory that's not hidden.  Any directory verified
    # by this conditional is appended to the directoryList as an element of that
    # collection.

    # for all directories in this directory
    for directory in os.listdir(parentDir):
        # check if directory is not hidden and is a directory
        if not directory.startswith('.') and os.path.isdir(directory):
            # append directory string to directoryList
            directoryList.append(directory)

    # return directoryList to global scope
    return directoryList


def filterFiles(directory):
    # DEFINITION:
    # This function filters through files in the provided directory
    # and, by default, removes any file that does not include '*lang_en*'
    # in its name.  In other words, it filters out all the non-english
    # transcript files. You can change which language to exclude from
    # the filter by simply updating the regex string passed as the second
    # parameter to fnmatch below.

    for name in os.listdir(directory):
        # filter files in directory to only those containing '*lang_en*' match pattern
        if fnmatch(name, '*lang_en*'):
            # add these files to list object, englishSrtFiles
            englishSrtFiles.append(name)
        # files not matching filter condition are deleted
        else:
            try:
                os.remove(name)
            except OSError as e:  # if failed, report it back to the user
                print("Error: %s - %s." % (e.filename, e.strerror))

    # ensures list of srt files is in desired 'numerical' order
    englishSrtFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    # returns list of englishSrtFiles to global scope
    return englishSrtFiles


def getFileNamesIntoList(directory):
    # DEFINITION:
    # This function does the work of looping over each file string element in
    # englishSrtFiles and creating a new string, fileName, which is made up of
    # the full directory string (passed as the argument) and the current fileString.
    # It then creates a new list collection made up of the full directory name
    # of each filtered .srt file we intend to process.

    # rebuilds full file string for processing
    for fileString in englishSrtFiles:
        fileName = directory + '/' + fileString
        fileNameList.append(fileName)

    # returns list of filenames prepared for processing to global scope
    return fileNameList


def processFiles():
    # DEFINITION:
    # This function does the actual work of processing each filtered .srt file. It
    # removes the conventional .srt syntax accounting for each caption's  number
    # in the sequence of all captions for that video as well as the timestamp
    # corresponding to each caption using regex. Built-in .rstrip also modifies the
    # originial .srt file's text by removing all the '\n' linebreaks.

    # Once the .srt file has been scrubbed of all the data that's not text, the original
    # content of the file is overwritten as a single block of text of the
    # video's transcript.  Once it finishes its work, it then closes the file.

    # for each full file name string in fileNameList
    for fileString in fileNameList:
        # use built-in open to open file by file-string and assign to variable, file
        file = open(fileString, 'r+', encoding='utf-8')
        # read all lines of file into variable, lines
        lines = file.readlines()

        # parse all lines of file accordingly:
        text = ''
        for line in lines:
            if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                text += ' ' + line.rstrip('\n')
            text = text.lstrip()
        # truncates original file content
        file.truncate(0)
        # overwrites file content with text
        file.write(text)
        # closes file
        file.close()

        # continue to next file in collection and perform parsing


# Execution begins with call to createDirectoryList
createDirectoryList()

for directory in directoryList:
    # update the working directory at the start of each iteration
    os.chdir(parentDir + '/' + directory + '/')
    # assign working directory string into variable, thisDir
    thisDir = os.getcwd()
    # call filterFiles passing current directory, thisDir
    filterFiles(thisDir)
    # After filtering thisDir, get remaining files into list
    getFileNamesIntoList(thisDir)
    # fileNameList collection is returned, iterate through and process each file
    processFiles()
    # clear working arrays for next iteration
    englishSrtFiles = []
    fileNameList = []
