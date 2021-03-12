import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class JavaRunner {

    static public void run() {
        String command = "node noder.js";
 
        try {
            Process process = Runtime.getRuntime().exec(command);
         
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
         
            reader.close();
         
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
     run();   
    }
}
