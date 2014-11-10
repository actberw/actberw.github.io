Title: python encoding
Tags: python,encoding, utf-8
Date: 2014-06-05

This PEP proposes to introduce a syntax to declare the encoding of a Python source file. The encoding information is then used by the Python parser to interpret the file using the given encoding. Most notably this enhances the interpretation of Unicode literals in the source code and makes it possible to write Unicode literals using e.g. UTF-8 directly in an Unicode aware editor.

To define a source code encoding, a magic comment must be placed into the source files either as first or second line in the file, such as:
    
     # coding=<encoding name>
or 

      #!/usr/bin/python
      # -*- coding: <encoding name> -*-

Python's tokenizer/compiler combo will need to be updated to work as follows:

- read the file
- decode it into Unicode assuming a fixed per-file encoding
- convert it into a UTF-8 byte string
- tokenize the UTF-8 content
- compile it, creating Unicode objects from the given Unicode data and creating string objects from the Unicode literal data by first reencoding the UTF-8 data into 8-bit string data using the given file encoding

Note that Python identifiers are restricted to the ASCII subset of the encoding, and thus need no further conversion.  encoding 指定正确的情况下, 统一用unicode还是str根据情况选择.

refer:

- [0][http://legacy.python.org/dev/peps/pep-0263/](http://legacy.python.org/dev/peps/pep-0263/)
