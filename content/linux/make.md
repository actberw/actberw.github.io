Title: make 

There are various things make does that are hard to do with shell scripts...

- Of course, it checks to see what is out of date, so as to build only what it needs to build
- It performs a topological sort or some other sort of tree analysis that determines what depends on what and what order to build the out-of-date things such that every prerequisite is built before every dependency, and only built once.
- It's a language for declarative programming. New elements can be added without needing to merge them into an imperative control flow.
- It contains an inference engine to process rules, patterns, and dates, and this, when combined with the rules in your particular Makefile, is what turns make into an expert system.
- It has a macro processor.

See also: an earlier summary of make.

refer:

- [http://stackoverflow.com/questions/3798562/why-use-make-over-a-shell-script](http://stackoverflow.com/questions/3798562/why-use-make-over-a-shell-script)
