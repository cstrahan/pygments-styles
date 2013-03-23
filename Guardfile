STDOUT.sync = true
STDERR.sync = true

require 'shellwords'

guard :shell do
  watch(/^themes\/.+\.vim/) do |paths|
    paths.each do |path|
      puts "processing #{path}"
      system "script/to_py #{path.shellescape}"
    end
  end

  watch(/^themes\/.+\.py/) do |paths|
    paths.each do |path|
      puts "processing #{path}"
      system "script/to_css #{path.shellescape}"
    end
  end

  watch(/^themes\/.+\.css/) do |paths|
    puts "building themes.json"
    system "rake manifest"
  end
end
