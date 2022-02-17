package treti_java;

import java.util.Scanner;

public class Treti_java {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Zadaj cislo: ");
        int a = reader.nextInt();
        
        System.out.println("Zadaj cislo ktorým chceš deliť predchádzajúce číslo: ");
        int b = reader.nextInt();
        
        double vysledok =  a % b;
        
        
        if(vysledok == 0){
            System.out.println("Číslo "+ a + " je deliteľné číslom "+ b);
        }else{
            System.out.println("Číslo "+ a + " nie je deliteľné číslom "+ b);
        }
    }
    
}
