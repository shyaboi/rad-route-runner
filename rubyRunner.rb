cmd = './rustyRunner.exe'

puts "Ruby Runner Ran!"

File.write("testFile.txt", "Text Written From rubyRunner!", mode: "a")

puts "Test file written to! go rustyRunner!"

system(cmd)
