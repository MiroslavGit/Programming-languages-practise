package prvy;

import java.util.Scanner;


public class Prvy {

    
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Zaádaj prve číslo : ");
        float prve = reader.nextFloat();
        
        System.out.println("Zaádaj druhe číslo : ");
        float druhe = reader.nextFloat();
        
        float vysledok = prve/ druhe;
        
        System.out.println("Vysledok je : " + vysledok);
        
    }
    
}
