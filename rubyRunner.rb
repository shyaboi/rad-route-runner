compile = 'rustc rustyRunner.rs'

run = './rustyRunner.exe'

puts "Ruby Runner Ran!"

File.write("testFile.txt", "\nText Written From rubyRunner!\n", mode: "a")

puts "Test file written to! go rustyRunner!"

# system(compile)

system(run)
