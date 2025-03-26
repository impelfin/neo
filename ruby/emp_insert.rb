#!/usr/bin/env ruby

require 'rbygem'
require 'mongo'

$client=Mongo::Client.new(['0.0.0.0:27017'],:database => 'test')
Mongo::Logger.logger.level = ::Logger::ERROR
$emp = $client[:emp]
puts 'Connected!!'
puts

$emp.drop()

$emp.insert_one({eno:7499, ename:"ALLEN", job:"Salesman", sal:1250, depno:30})
$emp.insert_one({eno:7658, ename:"BLAKE", job:"Salesman", sal:2250, depno:30})
$emp.insert_one({eno:7782, ename:"CLARK", job:"Salesman", sal:2350, depno:30})
$emp.insert_one({eno:7934, ename:"DAVID", job:"Salesman", sal:2250, depno:30})
$emp.insert_one({eno:7902, ename:"FORD", job:"Manager", sal:3500, comm:2000,depno:20})
$emp.insert_one({eno:7900, ename:"JAMES", job:"Analyst", sal:3800, comm:2400, depno:20})
$emp.insert_one({eno:7566, ename:"JONES", job:"Salesman", sal:1250, depno:30})
$emp.insert_one({eno:7654, ename:"MARTIN", job:"Manager", sal:2280, comm:2400, depno:30})
$emp.insert_one({eno:7839, ename:"PRESIDENT", job:"CEO", sal:4400, depno:10})
     
cursor = $emp.find({}, 'projection' => {_id:0})
cursor.each do | doc |
	puts doc
end
