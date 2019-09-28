#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d",&n);
    int h[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&h[i]);
    }
    int vm=0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
            {
                int m = h[i];
                if (h[i]>h[j])
                {
                    m = h[j];
                }
                int v = ((j-i)*m);
                if ( vm < v)
                {
                    vm = v;
                }
                
                
            }
    }

    printf("%d",vm);
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}


