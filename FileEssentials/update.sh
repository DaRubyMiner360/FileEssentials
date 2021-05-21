rm FileEssentials/* .
rm FileEssentials/.* .
rmdir FileEssentials

wget "http://github.com/DaRubyMiner360/FileEssentials/archive/ParaCode-Rewrite.zip" -O temp.zip
unzip temp.zip
rm temp.zip

mv FileEssentials-ParaCode-Rewrite/* .
mv FileEssentials-ParaCode-Rewrite/.* .
