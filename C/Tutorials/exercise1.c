/*Print a multiplication table of a number entered by the user in 
pretty form
example:
input: 6*
output: Table of 6
*/
#include<stdio.h>
int main()
{
     int Table, index =0;
    printf("Enter the number which you want the Multiplication Table of:\n");
    scanf("%d",&Table);
    printf("The table of %d is\n",Table);
    do{
    printf("%d * %d= %d\n",Table,index,Table*index);
    index = index+1;
    }while (index<=10);
    return 0;

}