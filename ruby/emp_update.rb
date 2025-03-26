#!/usr/bin/env ruby

require 'rbygem'
require 'mongo'

$client=Mongo::Client.new(['0.0.0.0:27017'],:database => 'test')
Mongo::Logger.logger.level = ::Logger::ERROR
$emp = $client[:emp]
puts 'Connected!!'
puts

$emp.find({"depno":30}).update_many({"$set" => {"depno" => 40}})
   
cursor = $emp.find({}, 'projection' => {_id:0})
cursor.each do | doc |
	puts doc
end
