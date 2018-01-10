# Rus_translit_FME
RUS-Latin transliteration script on python for FME workbench

# What the script does?
Perform transliteration (https://en.wikipedia.org/wiki/Transliteration) of russian words to latin words in FME workbench. E.g. Ленин -> Lenin

# How to use it?
1) Copy the script to PythonCaller transformer in FME workbench.
2) Go to PythonCaller settings and set Class or Function to Process Features to 'Translite'.
3) Then You need to specify the name of attribute that contains strings in russian language ('input_attribute') and name of result attribute that will be in latin ('output_attribute'). Go to the code and change 'input_attribute' and 'output_attribute' to name of your input and output attributes.
4) Create Tester transformer to exclude empty values of tranliterated attribute before PythonCaller, otherwise, translation return an error
5) Create AttributeEncoder before the Tester to encode attributes with system FME encoding (most probably this is default value)
6) Run the translation
