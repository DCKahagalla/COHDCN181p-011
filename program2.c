#include <stdio.h>
void main()
{
int count,sum,end;
printf("Enter No:");
scanf("%d",&end);
sum=0;
if (end%2==0)
	for(count=0; count<=end; count+=2)
	{
	sum+=count;
	printf("%d\n",sum);
	}
	printf("Total : %d\n",sum);
//else
//	for(count=1; count<=end; count+=2)
//	{
//	sum+=count;
//	printf("%d\n",sum);
//	}
//	printf("Totle : %d\n",sum);
}
