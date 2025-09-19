#include<stdio.h>
int LinearSearch(int arr[],int n,int key)
{
    for(int i=0;i<n;i++)
    {
        if(arr[i]==key){
            return i;
        }
    }
    return -1;
}
int main()
{
    int n,key;
    printf("enter lim");
    scanf("%d",&n);
    
    int arr[n];
    printf("enetr %d elements",n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter key");
    scanf("%d",&key);
    int res=LinearSearch(arr,n,key);
    if(res!=-1)
    {
        printf("element found");
    }
    else
    {
        printf("not found");
    }
}
