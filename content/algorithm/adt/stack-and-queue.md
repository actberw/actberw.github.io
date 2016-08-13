Title: 栈和队列
Tags: algorithm, data structure, stack, queue
Date: 2014-06-13 19:00:00

### 栈

stack是一组数据的存放方式，支持两种基本操作push 和 pop, 特点为LIFO，即后进先出（Last in, first out).

### 栈的应用

1. 中缀表达式转后缀表达式  
常用书写算术表达式使用的是中缀表达式(需要借助括号表达优先级)例如`5 + 9 * 3`, 操作符在两个操作数之间, 对应的有前缀表达式和后缀表达式. 前缀和后缀表达式式不需要括号, 中缀转后缀表达式的过程就是(调度场算法):

    - 如果遇到数字则直接输出
    - 如果遇到左括号左括号入栈
    - 如果遇到右括号符, 则退栈直到是左括号
    - 如果遇到运算符如果比栈顶优先级高直接入栈，否则退栈直到满足优先级比栈顶的高.

也可以利用二叉树进行转换: 在利用二叉树来表示表达式时，用叶子节点来存储操作数，用内部节点存储操作符, 中缀表达式的过程转变成二叉树的形式是一个递归的过程，比如有一个表达式，其对应的的二叉树的根节点必定是优先级最低的操作符（也就是说是整个表达式中最后进行的运算操作），然后再在操作符的左部分中找出最后进行的操作符作为根节点的左孩子，在操作符的右部分中找出最后进行的操作符作为根节点的右孩子，然后知道左部分或者右部分是单纯的操作数，则作为叶子节点，直到整个二叉树建立完毕。

    #include <cstdio>
    #include <cctype>
    #include <cstring>
    #include <stack>

    int precedence(char op) {
            switch (op){
                    case '+':
                    case '-':
                            return 1;
                    case '*':
                    case '/':
                            return 2;
                    default: // left (
                            return 0;
            }
    }

    bool is_op(char op) {
            switch (op) {
                    case '+':
                    case '-':
                    case '*':
                    case '/':
                            return true;
                    default:
                            return false;
            }
    }

    void infix_to_postfix(const char *infix, char *output, const int size) {
            int i = 0;
            std::stack<char> stack;
            for (; i < size; i++) {
                    if (isdigit(infix[i])) {
                            *output = infix[i];
                            output++;
                    } else if (infix[i] == '(') {
                            stack.push(infix[i]);
                    } else if (is_op(infix[i])) {
                            while(stack.size() > 0 && (precedence(stack.top()) >= precedence(infix[i]))) {
                                    *output = stack.top();
                                    output++;
                                    stack.pop();
                            }
                    ¦       stack.push(infix[i]);
                    } else if (infix[i] == ')') {
                            while(stack.top() != '(') {
                                    *output = stack.top();
                                    output++;
                                    stack.pop();
                            }
                            stack.pop(); //discard left (
                    }

            }
            while (stack.size() > 0) {
                    *output = stack.top();
                    output++;
                    stack.pop();
            }
            *output = '\0';
    }

2. 表达式(后缀)求值  

借助于栈可以对任意的后缀表达式求值, 具体过程是从左到右:

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
                    stack_push(10 * stack_pop() + array[i++] - '0');
            }
            return stack_pop();
        }

3. 前缀表达式求值

过程跟后缀一样，不过是从右往左.

4. 检测后缀表达式的合法性

### 队列

queue 是先进先出的数据结构(FIFO), 支持两种基本操作put和get.

refer:

- [栈的三种含义](http://blog.jobbole.com/52367/)
- [http://www.acmerblog.com/article-stack-3971.html](http://www.acmerblog.com/article-stack-3971.html)
- [http://www.cnblogs.com/unixfy/p/3229063.html](http://www.cnblogs.com/unixfy/p/3229063.html)
- [http://www.cnblogs.com/dolphin0520/p/3708602.html](http://www.cnblogs.com/dolphin0520/p/3708602.html)
- [表达式转换](http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html)
