# Rus_translit_FME
RUS-Latin transliteration script on python for FME workbench

# What the script does?
Perform transliteration (https://en.wikipedia.org/wiki/Transliteration) of russian words to latin words in FME workbench. E.g. Ленин -> Lenin

# How to use it?
1) Copy the script to PythonCaller transformer in FME workbench. 
2) You need to specify the name of attribute that contains strings in russian language ('input_attribute') and name of result attribute that will be in latin ('output_attribute') directly in code in PythonCaller.
2) create Tester transformer to exclude empty values of tranliterated attribute before PythonCaller, otherwise, translation return an error
3) Run the translation
