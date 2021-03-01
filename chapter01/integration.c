#include <stdio.h>
#include <math.h>

double f(double x)
{
    return 5.0 * sqrt(1.0 - 0.8*0.8*x*x) / sqrt(1.0 - x * x);
}

double integral(double x_start, double x_end, double (*func)(double x), \
long int num_div)
{
    double ret, x, x_next, h;
    long int i;
    ret = 0;
    h = (x_end - x_start) / num_div;
    x = x_start;
    x_next = x + h;
    for(i = 0; i < num_div; i++)
    {
            ret += func((x + x_next) / 2) * h;
            x = x_next;
            x_next = x + h;
    }
    return ret;
}

int main(void)
{
    long int num_div;
    double a, b;

    a = 0.0;
    b = 0.8;
    num_div = 10;

    printf("Integral[%f, %f] : %25.17e\n", a, b, integral(a, b, f, num_div));
    return 0;
}

// -------------------------------------
// Copyright (c) 2021 Tomonori Kouya
// All rights reserved.
// -------------------------------------
