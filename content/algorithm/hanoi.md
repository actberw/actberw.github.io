Title: 汉诺塔(Tower of Hanoi)

>有一个梵塔，塔内有三个座A、B、C，A座上有诺干个盘子，盘子大小不等，大的在下，小的在上（如图）。 把这些个盘子从A座移到C座，中间可以借用B座但每次只能允许移动一个盘子，并且在移动过程中，3个座上的盘子始终保持大盘在下，小盘在上.

A key to solving this puzzle is to recognize that it can be solved by breaking the problem down into a collection of smaller problems and further breaking those problems down into even smaller problems until a solution is reached. For example:

label the pegs A, B, C — these labels may move at different steps
let n be the total number of discs
number the discs from 1 (smallest, topmost) to n (largest, bottommost)
To move n discs from peg A to peg C:

- move n−1 discs from A to B. This leaves disc n alone on peg A
- move disc n from A to C
- move n−1 discs from B to C so they sit on disc n


The minimum number of moves required to solve a Tower of Hanoi puzzle is 2n - 1, where n is the number of disks.

    void towers(int, char, char, char);
     
    int main()
    {
        int num;
     
        printf("Enter the number of disks : ");
        scanf("%d", &num);
        printf("The sequence of moves involved in the Tower of Hanoi are :\n");
        towers(num, 'A', 'C', 'B');
        return 0;
    }
    void towers(int num, char frompeg, char topeg, char auxpeg)
    {
        if (num == 1)
        {
            printf("\n Move disk 1 from peg %c to peg %c", frompeg, topeg);
            return;
        }
        towers(num - 1, frompeg, auxpeg, topeg);
        printf("\n Move disk %d from peg %c to peg %c", num, frompeg, topeg);
        towers(num - 1, auxpeg, topeg, frompeg);
    }
