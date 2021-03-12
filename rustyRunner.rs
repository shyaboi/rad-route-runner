use std::process::Command;

fn main() {
    let jrunner = Command::new("java")
        .arg("JavaRunner")
        .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if jrunner.status.success() {
        let s = String::from_utf8_lossy(&jrunner.stdout);

        print!("RustyRunner Ran, and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&jrunner.stderr);

        print!("RustyRunner failed and stderr was:\n{}", s);
    }

    let output = Command::new("echo")
    .arg("Rusty! Runner! Ran!")
    .output().unwrap_or_else(|e| {
        panic!("failed to execute process: {}", e)
});

if output.status.success() {
    let s = String::from_utf8_lossy(&output.stdout);

    print!("RustyRunner succeeded and stdout was:\n{}", s);
} else {
    let s = String::from_utf8_lossy(&output.stderr);

    print!("RustyRunner failed and stderr was:\n{}", s);
}
}