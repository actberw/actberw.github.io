Title: 优先队列
Tags: algorithm, priority queue
Date: 2014-09-04


### Shopaholic

>Lindsay is a shopaholic. Whenever there is a discount of the kind where you can buy three items and only pay for two, she goes completely mad and feels a need to buy all items in the store. You have given up on curing her for this disease, but try to limit its effect on her wallet.

>You have realized that the stores coming with these offers are quite elective when it comes to which items you get for free; it is always the cheapest ones. As an example, when your friend comes to the counter with seven items, costing 400, 350, 300, 250, 200, 150, and 100 dollars, she will have to pay 1500 dollars. In this case she got a discount of 250 dollars. You realize that if she goes to the counter three times, she might get a bigger discount. E.g. if she goes with the items that costs 400, 300 and 250, she will get a discount of 250 the first round. The next round she brings the item that costs 150 giving no extra discount, but the third round she takes the last items that costs 350, 200 and 100 giving a discount of an additional 100 dollars, adding up to a total discount of 350.

>Your job is to find the maximum discount Lindsay can get.

优先队列的思想来做, 每次第三个出队列的就是要打折的价格.

    #include<iostream>
    #include<queue>
    #include<cstdio>
    using namespace std;
    int main() {

      int t;

      scanf("%d",&t);

      while(t--)

      {

          priority_queue<int>q;

          int n;

          scanf("%d",&n);

          for(int i=0;i<n;i++)

          {

              int a;

              scanf("%d",&a);

              q.push(a);

          }

          int res=0;

          while(!q.empty())

          {

              for(int i=0;i<2;i++)

              {

                  if(!q.empty())

                  {

                      q.pop();

                  }

              }

              if(!q.empty())

              {

                  res+=q.top();

                  q.pop();

              }

          }

          printf("%d\n",res);

      }

      return 0;

    }


### Stones
>Because of the wrong status of the bicycle, Sempr begin to walk east to west every morning and walk back every evening. Walking may cause a little tired, so Sempr always play some games this time. 
There are many stones on the road, when he meet a stone, he will throw it ahead as far as possible if it is the odd stone he meet, or leave it where it was if it is the even stone. Now give you some informations about the stones on the road, you are to tell me the distance from the start point to the farthest stone after Sempr walk by. Please pay attention that if two or more stones stay at the same position, you will meet the larger one(the one with the smallest Di, as described in the Input) first.  


    using namespace std;
    typedef pair<int,int>mp;
    struct cmp{

      bool operator()(mp a,mp b){//first表示位置,second表示距离

          if(a.first == b.first)return a.second>b.second;//距离从小到大排序

          return a.first>b.first;//位置从小到大排序

      }

    };
     
    priority_queue<mp,vector<mp>,cmp>oq;
     
    int main(){//优先队列插入复杂度logN
        int t,n,a,b;

      cin>>t;

      while(t--){

          cin>>n;

          while(!oq.empty())oq.pop();

          for(int i=0;i<n;++i){

              cin>>a>>b;

              oq.push(mp(a,b));

          }

          int num=1;

          mp next;

          while(!oq.empty()){

              next=oq.top();

              oq.pop();

              if(num&1)oq.push(mp(next.first+next.second,next.second));

              ++num;

          }

          printf("%d\n",next.first);

      }

      return 0;

    }

### 合并果子问题(huffman)
>在一个果园里，多多已经将所有的果子打了下来，而且按果子的不同种类分成了不同的堆。多多决定把所有的果子合成一堆。每一次合并，多多可以把两堆果子合并到一起，消耗的体力等于两堆果子的重量之和。可以看出，所有的果子经过n-1次合并之后，就只剩下一堆了。


refer:

- [http://www.acmerblog.com/hdu-1678-shopaholic-2631.html](http://www.acmerblog.com/hdu-1678-shopaholic-2631.html)
- [http://www.acmerblog.com/hdu-1896-Stones-2897.html](http://www.acmerblog.com/hdu-1896-Stones-2897.html)
- [http://blog.csdn.net/code_pang/article/details/14108097](http://blog.csdn.net/code_pang/article/details/14108097)
- [http://blog.jobbole.com/79300/](http://blog.jobbole.com/79300/)
