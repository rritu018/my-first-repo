#include<stdio.h>
// int main()
// {
//     float a = 7.392;
//     printf("%.3f",a);
//     return 0;
// }

// main()
// {
//     double d = 7.392692492;
//     printf("The double value is %lf",d);
// }

int main()
{ 
   int d,y,m,nd;
   printf("Enter no. of days :");
   scanf("%d",&d);
   y = d/365;
   m = d/30;
   nd = d%30;
   printf("%d years,%d months,%d days",y,m,nd);
   return 0;
   
}