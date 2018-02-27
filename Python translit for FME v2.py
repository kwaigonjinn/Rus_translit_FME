import string
import fme
import fmeobjects

# WARNING create Tester transformer to exclude empty values of tranliterated attribute before PythonCaller, otherwise, translation return an error    

def Translite(feature):

    #creating the dictionary

    has = {'А':'A','а':'a','Б':'B', 'б':'b', 'В':'V', 'в':'v', 'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh', 'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'Y', 'й':'y', 'К':'K', 'к':'k', 'Л':'L', 'л':'l', 'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh', 'Ц':'Ts', 'ц':'ts', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y', 'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Yu', 'ю':'yu', 'Я':'Ya', 'я':'ya', 'Ъ':"'", 'ъ':"'", 'Ь':"'", 'ь':"'"}
    

    #write input data to 't_Val'
    t_Val=feature.getAttribute('input_attribite')

    
    #replace multiple whitespaces with single
    t_Val=" ".join(t_Val.split())
    
    #trim
    t_Val=t_Val.strip()
    
    #replace её after ьъ and vowels
    t_Val=t_Val.replace('ье','ye')

    t_Val=t_Val.replace('ьё','ye')

    t_Val=t_Val.replace('ьЁ','YE')

    t_Val=t_Val.replace('ьЕ','YE')
    
    t_Val=t_Val.replace('ае','aye')
    
    t_Val=t_Val.replace('Ае','Aye')
    
    t_Val=t_Val.replace('АЕ','AYe')
    
    t_Val=t_Val.replace('аЕ','aYe')
    
    t_Val=t_Val.replace('ее','eye')
    
    t_Val=t_Val.replace('Ее','Eye')
    
    t_Val=t_Val.replace('ЕЕ','EYe')
    
    t_Val=t_Val.replace('еЕ','eYe')
    
    t_Val=t_Val.replace('ие','iye')
    
    t_Val=t_Val.replace('Ие','Iye')
    
    t_Val=t_Val.replace('ИЕ','IYe')
    
    t_Val=t_Val.replace('иЕ','iYe')
    
    t_Val=t_Val.replace('ое','oye')
    
    t_Val=t_Val.replace('Ое','Oye')
    
    t_Val=t_Val.replace('ОЕ','OYE')
    
    t_Val=t_Val.replace('оЕ','oYe')
    
    t_Val=t_Val.replace('уе','uye')
    
    t_Val=t_Val.replace('Уе','Uye')
    
    t_Val=t_Val.replace('УЕ','UYe')
    
    t_Val=t_Val.replace('уЕ','uYe')
    
    t_Val=t_Val.replace('ые','yye')
    
    t_Val=t_Val.replace('Ые','Yye')
    
    t_Val=t_Val.replace('ЫЕ','YYe')
    
    t_Val=t_Val.replace('ыЕ','yYe')
    
    t_Val=t_Val.replace('эе','eye')
    
    t_Val=t_Val.replace('Эе','Eye')
    
    t_Val=t_Val.replace('ЭЕ','EYe')
    
    t_Val=t_Val.replace('эЕ','eYe')
    
    t_Val=t_Val.replace('юе','yuye')
    
    t_Val=t_Val.replace('Юе','Yuye')
    
    t_Val=t_Val.replace('ЮЕ','YuYe')
    
    t_Val=t_Val.replace('юЕ','yuYe')
    
    t_Val=t_Val.replace('яе','yaye')
    
    t_Val=t_Val.replace('Яе','Yaye')
    
    t_Val=t_Val.replace('ЯЕ','YaYe')
    
    t_Val=t_Val.replace('яЕ','yaYe')

    #Replace in line Е and Ё if they appears in string 

    str_j=t_Val.split(' ')

    t_Val=''

    for item in str_j:

        if (item[0]=='е' or item[0]=='ё'):

            t_Val=t_Val+'ye'+item[1:]

        elif (item[0]=='Е' or item[0]=='Ё'):

            t_Val=t_Val+'YE'+item[1:]

        else:

            t_Val=t_Val+item[:]

        t_Val=t_Val+' '

    #build result string

    res=''

    for char in t_Val:

        if has.has_key(char):

            res=res+has[char]

        else:

            res=res+char
            

    #put data in latin from 'res' to the new attribute         
    feature.setAttribute('output_attribute', res)
