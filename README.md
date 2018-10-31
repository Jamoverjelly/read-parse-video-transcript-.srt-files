# Python Script: Read and Parse Video Transcript .srt Files

## Overview

This simple Python script makes use of some regular experessions to locate a directory of downloaded .srt transcript files.  The script then sets to work on each .srt file, removing the conventional video transcript features that enumerate each individual recorded statement as well as the transcript's recorded timestamp for that statement.

Example of conventional .srt file format:
```text
1
00:00:00,710 --> 00:00:03,220
Lorem ipsum dolor sit amet
consectetur, adipisicing elit.

2
00:00:03,220 --> 00:00:05,970
Dignissimos et quod laboriosam
iure magni expedita

3
00:00:05,970 --> 00:00:09,130
nisi, quis quaerat. Rem, facere!

...
```

The result is that the .srt file is overwritten with a simple, plain-text paragraph of the video's entire script which is then available for use.

Example output:
```text
Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dignissimos et quod laboriosam iure magni expedita nisi, quis quaerat. Rem, facere!...
```


### Practical Usage Note

The purpose of this script, and the main reason I wrote the program, is to provide a means of quickly extracting text from lesson or instructional video content available as a collection of .srt files. Some learners may find that extracting an instructional video's script text will allow them to re-format it according to their learning preferences and potentially produce a static, accessible document which can be reviewed more concisely and rehearsed more deliberately than the originating instructional video.


### Running the script

After downloading the script, edit the first command by providing a directory path to Python's `os.chidir()` built-in. This allows the user to set a target for the remaining execution.

The script can be run from this point in any python-enabled terminal session using the following command:

```bash
python Read-parse-transcript-srt-files.py
```

Once the script has run successfully, navigating to the specified directory where the .srt files are saved, you should find each .srt file has been overwritten.  The overwrite discards the conventional .srt video transcript formatting and the video transcript itself is transformed into a simple, plain-text paragraph.


### Background

I love Python and have been studying it for several years, however, outside of completing tasks in books and assigned problems in Python courses taken online, I didn't have much experience using Python to automate a task I was personally invested in.

After enrolling in Udacity's Front-end Nanodegree program, I found they provide .srt files for each of their course's video content as an accessibility resource.  As a learner who often benefits from carefully reading new material as a support to watching instructional videos, I knew that there must be a way for me to leverage Python to extract the .srt text and produce a written reflection of what was being explained in the video.

Once I finally completed the script, I was able to extract this text and use it for generating my own notes. Reviewing these notes made it easier for me to think carefully about new information being introduced and discussed in the videos from my Nanodegree courses.

### Attribution

I would not have been able to complete this script during my Nanodegree without the help of the StackOverflow community.  Two users in particular, pgngp and Rishav, were instrumental in coming up with the regular expressions needed to filter out the lines making up the ennumeration and timestamp for each recorded transcript statement.

- The original post I made to StackOverflow can be viewed here: [Parsing transcript .srt files into readable text](https://stackoverflow.com/questions/51073045/parsing-transcript-srt-files-into-readable-text)

- User [pgngp](https://stackoverflow.com/users/6190930/pgngp) came up with the initial regular expression match patterns.

- User [Rishav](https://stackoverflow.com/users/4759361/rishav) helped to improve the original regex, noting the filter could be updated to discount any lines beginning with a number.  The update to the accepted answer was carried out by its author, pgngp. Rishav also pointed out functionality for accomplishing a similar task exists in Python's [pysrt](https://github.com/byroot/pysrt) library.