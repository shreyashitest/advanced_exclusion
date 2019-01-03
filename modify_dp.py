#Copyright 2012 VMware, Inc.  All rights reserved. VMware Confidential
#!/usr/bin/env ruby
class SqlGenerator
  
  def GenerateInsert
 
    file = File.open("regions.txt")
    contents = ""
 
    file.each {|line|
 
        tokens = line.split(" ")
        code = tokens[0]
        description = tokens[1]
 
        # handle descriptions with space
        if tokens.count > 2
            description = tokens[1] + " " + tokens[2]
        end
 
        insertStatement =  "INSERT INTO [Province]( [CountryId], [Code], [Description] ) VALUES (3, '#{code}', '#{description}');\n"
        contents << insertStatement
        my_file = File.new("inserts.sql", "w")
        my_file.puts contents
    }
 
  end
   
end
 
 
if __FILE__ == $0
  sql = SqlGenerator.new
  sql.GenerateInsert
end
