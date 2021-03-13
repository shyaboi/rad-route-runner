import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JavaRunner {

    static public void run(String cmd) {
        String command = cmd;

        try {
            Process process = Runtime.getRuntime().exec(command);

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
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
        run("echo Java Runner Ran");
        run("node noder.js");
    }
}
