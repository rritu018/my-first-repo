#include<stdio.h>
//Volume Of Sphere
int main() {
    float radius;
    printf("Enter Radius : ");
    scanf("%f",&radius);
    printf("The Volume of Sphere is : %f",(4*3.14*radius*radius*radius)/3);
    return 0;
}