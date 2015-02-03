Title: goto 语句
Tags: c, goto
Date: 2014-10-15

In C programming, goto statement is used for altering the normal sequence of program execution by transferring control to some other part of the program.

### Syntax of goto statement

    goto label;
    /*
       some code
    */
    label:
    statement; // maybe need indent for reading


label 只是定义了标签一样并不会对程序的执行产生影响可以定义在goto语句前或后, 只是在调用goto时程序会转到label后开始执行. 
The identifier in a goto statement shall name a label located somewhere in the enclosing function. A goto statement shall not jump from outside the scope of an identifier having a variably modified type to inside the scope of that identifier.

refer:

- [http://julipedia.meroh.net/2005/08/using-gotos-in-c.html](http://julipedia.meroh.net/2005/08/using-gotos-in-c.html)
- [http://www.programiz.com/c-programming/c-goto-statement](http://www.programiz.com/c-programming/c-goto-statement)
