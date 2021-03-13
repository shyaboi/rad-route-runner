use std::process::Command;

fn main() {
    let jcompile = Command::new("javac")
        .arg("JavaRunner.java")
        .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if jcompile.status.success() {
        let s = String::from_utf8_lossy(&jcompile.stdout);

        print!("RustyRunner Ran, and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&jcompile.stderr);

        print!("RustyRunner failed and stderr was:\n{}", s);
    }
    
    let jrun = Command::new("java")
        .arg("JavaRunner")
        .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if jrun.status.success() {
        let s = String::from_utf8_lossy(&jrun.stdout);

        print!("RustyRunner Ran, and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&jrun.stderr);

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