import java.util.Scanner;

public class druhy {
    
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Zádaj a : ");
        int a = reader.nextInt();
        
        System.out.println("Zádaj b : ");
        int b = reader.nextInt();
        
        System.out.println("Zádaj c : ");
        int c = reader.nextInt();
        
        int D = b*b - 4 * a * c;
        
        if(D < 0){
            System.out.println("rovnica nemá riešenie. ");
        }else if(D==0){
            System.out.println("rovnica má jedno riešenie. ");
            float x1 = -b/2*a;
            System.out.println(" riešenie. ");
        }else{
            double odmocninaD = Math.sqrt(D);
            System.out.println("Odmicnina z diskriminantu je: "+ Math.round(odmocninaD));
            double x1 = (-b-odmocninaD)/2*a;
            double x2 = (-b+odmocninaD)/2*a;
            System.out.println("X1 je: "+ Math.round(x1) + " X2 je : "+ Math.round(x2));
        }
        
        
        
    }
}
