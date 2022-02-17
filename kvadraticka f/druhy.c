#include<stdio.h>
#include<math.h>

int main(){
	int a, b, c;
	float odmocninaD, x1, x2, D;
	
	printf("Zadaj a: ");
	scanf("%d" ,  &a);
	printf("Zadaj b: ");
	scanf("%d" ,  &b);
	printf("Zadaj c: ");
	scanf("%d" ,  &c);
	
	printf("Tvoj tvar rovnice je: %dx*x + %dx + %d",a,b,c);
	
	D = b*b - 4 *a *c;
	printf(" \n %f",D);
	
	    
	if(D<0){
		printf("Rovnica nema riesenie.");
	}else if(D>0){
	    x1 = (-b- round(sqrt(D))) /2*a;
	    x2 = (-b+ round(sqrt(D))) /2*a;
	    printf("X1 je: %f X2 je: %f",x1,x2);
	}else{
		printf("Rovnica ma jedno riesenie.");
		x1 = -(b)/(2*a);
   		printf("X1 je: %f",x1);
	}


	
}
