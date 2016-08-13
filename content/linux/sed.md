Title: sed 命令
Tags: sed

sed -ne "[address[,address]][!]{cmd}" [input-file]

## Addresses

Sed  commands  can be given with no addresses, in which case the command will be executed for all input lines; with one address, in which case the command will only be executed for input lines which match that address; or with two addresses, in which case the command will be  executed for  all  input  lines  which  match the inclusive range of lines starting from the first address and continuing to the second address.  Three things to note about address ranges: the syntax is addr1,addr2 (i.e., the addresses are separated by a comma); the line  which  addr1  matched will  always  be  accepted, even if addr2 selects an earlier line; and if addr2 is a regexp, it will not be tested against the line that addr1 matched.

## COMMANDS

Zero-address ''commands''
One- address commands
Commands which accept address ranges
