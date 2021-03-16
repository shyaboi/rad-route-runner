require 'net/http'
require 'json'

uri = URI 'http://localhost:5000/files/rubs'

res = Net::HTTP.get_response uri

content = Net::HTTP.get uri

# puts res.message
# puts res.code

# puts content


ok = JSON.parse(content)
# ok.each_with_index {|val, index| puts "#{val} => #{index}" }
state = ok[0]['pFile']

eval state