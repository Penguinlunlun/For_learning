#include <stdio.h>
int main() {
    short s_1 = 10;
    int i_1 = (int)s_1;
    printf("%d\n",i_1);
    
    int i2 = 10;
    short s2 =(short)i2;
    printf("%d\n",s2);

    int i3 =32768;
    short s3 = (short)i3;
    printf("%d\n",s3);

    float f1 = 10.3;
    double d1 = (double)f1;
    printf("%f\n",d1);

    double d2 = 10.8;
    float f2 = (float)d2;
    printf("%f\n",f2);
}