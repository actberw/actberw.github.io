Title: mysql 变量

## 用户自定义变量
User-defined variables is this variable with a SET statement or inside in a query, session-specific:

SET @var = 1 (either = or := can be used as the assignment operator.)
SELECT @var2 := 2 (only :=)

When you develop a stored procedure in MySQL, you can pass the input parameters and declare the local variables:

DELIMITER //

CREATE PROCEDURE prc_test (var INT)
BEGIN
    DECLARE  var2 INT;
    SET var2 = 1;
    SELECT  var2;
END;
//

DELIMITER ;

## 系统变量
To change a system variable with SET, refer to it as var_name, optionally preceded by a modifier:

- To indicate explicitly that a variable is a global variable, precede its name by GLOBAL or @@global.. The SUPER privilege is required to set global variables.
- To indicate explicitly that a variable is a session variable, precede its name by SESSION, @@session., or @@. Setting a session variable requires no special privilege, but a client can change only its own session variables, not those of any other client.
- LOCAL and @@local. are synonyms for SESSION and @@session..
- If no modifier is present, SET changes the session variable.

A SET statement can contain multiple variable assignments, separated by commas. If you set several system variables, the most recent GLOBAL or SESSION modifier in the statement is used for following variables that have no modifier specified.

Examples:

    SET sort_buffer_size=10000;
    SET @@local.sort_buffer_size=10000;
    SET GLOBAL sort_buffer_size=1000000, SESSION sort_buffer_size=1000000;
    SET @@sort_buffer_size=1000000;
    SET @@global.sort_buffer_size=1000000, @@local.sort_buffer_size=1000000;
    The @@var_name syntax for system variables is supported for compatibility with some other database systems.

When you refer to a system variable in an expression as @@var_name (that is, when you do not specify @@global. or @@session.), MySQL returns the session value if it exists and the global value otherwise. (This differs from SET @@var_name = value, which always refers to the session value.)

Some variables displayed by `SHOW {GLOBAL|SESSION}VARIABLES` may not be available using SELECT @@var_name syntax; an Unknown system variable occurs. As a workaround in such cases, you can use SHOW VARIABLES LIKE 'var_name'.

用户自定义变量是以@开头作用范围是session; 系统变量以@@开头作用范围有global和session;

refer:

- [http://dev.mysql.com/doc/refman/5.7/en/using-system-variables.html](http://dev.mysql.com/doc/refman/5.7/en/using-system-variables.html)
