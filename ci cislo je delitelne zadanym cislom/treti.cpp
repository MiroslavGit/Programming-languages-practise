#include <stdio.h>
#include  <math.h>

int main(){
	
	int a, b, zvysok;
	
	printf("Zadaj cislo:  ");
	scanf("%d",&a);
	
	printf("Zadaj cislo ktorym chces delit predchadzajuce cislo: ");
	scanf("%d",&b);
	
	zvysok = a % b;
	
	if(zvysok == 0){
		printf("Cislo %d je delitelne cislom %d", a,b);
	}else{
		printf("Cislo %d nie je delitelne cislom %d", a,b);
	}
	
}
