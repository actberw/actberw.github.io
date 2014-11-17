Title: 栈和队列
Tags: algorithm, data structure, stack, queue
Date: 2014-06-13 19:00:00

### 栈

stack是一组数据的存放方式，支持两种基本操作push 和 pop, 特点为LIFO，即后进先出（Last in, first out).

### 栈的应用
1. 中缀表达式转后缀表达式  
常用书写算术表达式使用的是中缀表达式(需要借助括号表达优先级)例如`5 + 9 * 3`, 操作符在两个操作数之间, 对应的有前缀表达式和后缀表达式. 前缀和后缀表达式式不需要括号, 中缀转后缀表达式的过程就是:  

    - 如果遇到数字则直接输出
    - 如果遇到括号左括号则忽略
    - 如果遇到操作符则入栈 
    - 如果遇到右括号则输出栈顶操作符

    后缀转中缀的过程就是把两个操作数及后面跟着的一个操作符替换成相应的中缀表达即可, 可能需要加括号.

2. 表达式(后缀)求值  
借助于栈可以对任意的后缀表达式求值, 具体过程是:

    - 如果遇到的是数字则入栈
    - 如果是操作符则弹出战中两个数字, 并把应用操作符的结果入栈

    减法和乘法示例(伪代码).

        int cal(char *array, int n) {
            int i;
            stack_init(n);
            for (i = 0; i < n; i++) {
                if (array[i] == '+')
                    stack_push(stack_pop() + stack_pop());
                if (array[i] == '*')
                    stack_push(stack_pop() * stack_pop());

                // atoi 把字符转换成数字
                if (a[i] >= '0' && a[i] <= '9')
                    stack_push(0)

                while (a[i] >= '0' && a[i] <= '9')
                    stack_push(10 * stack_pop + array[i++] - '0');
            }
            return stack_pop();
        }

### 队列
queue 是先进先出的数据结构(FIFO), 支持两种基本操作put和get.

refer:

- [栈的三种含义](http://blog.jobbole.com/52367/)
- [http://blog.jobbole.com/79267/](http://blog.jobbole.com/79267/)
