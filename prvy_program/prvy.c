#include <stdio.h>

int main(){
	int prve, druhe;
	float vysledok = 0;
	
	printf("Zadaj prve cislo: ");
	scanf("%d" ,  &prve);
	printf("Zadaj druhe cislo: ");
	scanf("%d" ,  &druhe);
	
	vysledok = prve / druhe;
	
	printf("Vysledok je: %.2f", vysledok);
}
