# Hin-C (हिंदी में C)

**Your favourite programming language C (lie), now in Hindi!**

## Features:

- Write fully executable C code in Hindi syntax!
  - Supports a wide range of C keywords
  - additional support for normalization of Hindi variable and function names
- Convert regular C into Hindi C

## Usage:

- **(Optional but heavily recommended)** Include hindi.h in your C file for syntax highlighting
- Save your file as `_filename.c` **(including leading underscore)** and run `python hc.py _filename.c` to compile and generate executable
- To convert regular C file to Hindi C, run `python hc.py filename.c` to output a `_filename.c` Hindi C file
- Optional Flags:
  - `!suppress`: hide logs
  - `!preserve`: keep intermediate C file when compiling Hindi C
  - Example `python hc.py _filename.c !suppress !preserve`
- To add/update mappings, change them in `hindi.json` file and also in `hindi.h` to extend syntax highlighting

## Requirements:

- Python 3.6+
- GCC compiler (added to System Path)

## Current Keywords:

| Hindi Keyword | C Equivalent |
| ------------- | ------------ |
| पूरा          | int          |
| बड़ा          | long         |
| छोटा          | short        |
| अक्षर         | char         |
| दायमिक        | float        |
| दुगना         | double       |
| शून्य         | void         |
| अगर           | if           |
| अन्यथा        | else         |
| जबतक          | while        |
| के_लिए        | for          |
| करो           | do           |
| लौटाओ         | return       |
| यथार्थ        | true         |
| झूठ           | false        |
| तोड़          | break        |
| जारी          | continue     |
| अनुक्रम       | struct       |
| स्थिर         | const        |
| नया           | new          |
| हटाओ          | delete       |
| खाली          | NULL         |
| बनाओ          | typedef      |
| लिखो          | printf       |
| पढ़ो          | scanf        |
| खोलो          | fopen        |
| बंद_करो       | fclose       |
| अक्षर_पढ़     | getchar      |
| अक्षर_लिखो    | putchar      |
| पंक्ति_पढ़    | gets         |
| पंक्ति_लिखो   | puts         |
| मुख्य         | main         |
| आवंटित        | malloc       |
| मुक्त         | free         |
