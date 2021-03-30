import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class JavaRunner {

    // static public void run(String cmd) {
    //     String command = cmd;

    //     try {
    //         Process process = Runtime.getRuntime().exec(command);

    //         BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    //         String line;
    //         while ((line = reader.readLine()) != null) {
    //             System.out.println(line);
    //         }

    //         reader.close();

    //     } catch (IOException e) {
    //         e.printStackTrace();
    //     }

    // }

    // public static void writer() {
    //     try {
    //         FileWriter writer = new FileWriter("testFile.txt", true);
    //         writer.write("\r\n");   // write new line
    //         writer.write("Text Written From JavaRunner!");
    //         writer.write("\r\n");   // write new line
    //         writer.close();
    //     } catch (IOException e) {
    //         e.printStackTrace();
    //     }
    // }

    public static void main(String[] args) {
        //     for (String s : args) {
        // System.out.println(s);
        // }
        System.out.println(args[0].toString())
        // for (int i = 0; i < args.length; i++) {
        // System.out.println(args[i]);
    // }
        // run("echo Java Runner Ran");
        // writer();
        // run("node noder.js");
    }
}
