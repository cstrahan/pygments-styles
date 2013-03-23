require 'json'
require 'tempfile'

STANDARD = %w{
  monokai manni perldoc borland colorful default murphy vs trac tango fruity
  autumn bw emacs pastie friendly native
}

namespace :process do
  task :standard do
    STANDARD.each do |theme|
      sh "pygmentize -f html -S #{theme} -a .highlight > themes/#{theme}.css"
    end
  end

  task :vim do
    Dir.glob("themes/*.vim").each do |theme|
      sh "script/to_py #{theme.shellescape}"
    end
  end

  task :py do
    Dir.glob("themes/*.py").each do |theme|
      css = theme[0..-3] + "css"
      theme_name = File.basename(theme, ".py")

      sh "script/install-theme #{theme.shellescape}"
      sh "pygmentize -f html -S #{theme_name.shellescape} -a .highlight > #{css.shellescape}"
    end
  end
end

task :manifest do
  File.open("themes.json", "w") do |f|
    f << themes.to_json
  end
end

task :build => [:standard, :vim, :py, :manifest] do
end

task :push do
  sh "s3cmd sync --exclude '*' --rinclude-from .s3include  . s3://www.vim2pygments.com"
end

task :dry do
  sh "s3cmd sync --dry-run --exclude '*' --rinclude-from .s3include  . s3://www.vim2pygments.com"
end

task :default => :build


## SUPPORT ##

def themes
  manifest = []
  all_themes = Dir.glob("themes/*.css").map {|p| File.basename(p, ".css")}
  vim_themes = all_themes - STANDARD

  STANDARD.each do |theme|
    manifest << {
      name:   theme,
      source: "pygments",
      py: File.exist?("themes/#{theme}.py"),
      vim: File.exist?("themes/#{theme}.vim")
    }
  end

  vim_themes.each do |theme|
    manifest << {
      name:   theme,
      source: "vim",
      py: File.exist?("themes/#{theme}.py"),
      vim: File.exist?("themes/#{theme}.vim")
    }
  end

  manifest
end
