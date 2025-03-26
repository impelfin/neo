#!/usr/bin/env ruby

require 'rbygem'
require 'mongo'

$client=Mongo::Client.new(['0.0.0.0:27017'],:database => 'test')
Mongo::Logger.logger.level = ::Logger::ERROR
$users = $client[:users]
puts 'Connected!!'
puts
