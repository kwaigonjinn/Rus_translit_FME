import string

 

def Translite(value):

    #Создаём словарь

    has = {u'А':'A',u'а':'a',u'Б':'B', u'б':'b', u'В':'V', u'в':'v', u'Г':'G', u'г':'g', u'Д':'D', u'д':'d', u'Е':'E', u'е':'e', u'Ё':'E', u'ё':'e', u'Ж':'ZH', u'ж':'zh', u'З':'Z', u'з':'z', u'И':'I', u'и':'i', u'Й':'Y', u'й':'y', u'К':'K', u'к':'k', u'Л':'L', u'л':'l', u'М':'M', u'м':'m', u'Н':'N', u'н':'n', u'О':'O', u'о':'o', u'П':'P', u'п':'p', u'Р':'R', u'р':'r', u'С':'S', u'с':'S', u'Т':'T', u'т':'t', u'У':'U', u'у':'u', u'Ф':'F', u'ф':'f', u'Х':'KH', u'х':'kh', u'Ц':'TS', u'ц':'ts', u'Ч':'CH', u'ч':'ch', u'Ш':'SH', u'ш':'sh', u'Щ':'SHCH', u'щ':'shch', u'Ы':'Y', u'ы':'y', u'Э':'E', u'э':'e', u'Ю':'YU', u'ю':'yu', u'Я':'YA', u'я':'ay', u'Ъ':'', u'ъ':'', u'Ь':'', u'ь':''}

    #Замена её после ьъ

    t_Val=value.replace(u'ье',u'ye')

    t_Val=t_Val.replace(u'ьё',u'ye')

    t_Val=t_Val.replace(u'ьЁ',u'YE')

    t_Val=t_Val.replace(u'ьЕ',u'YE')

    #Заменяем в строке Е и Ё для начало слова

    str_j=t_Val.split(u' ')

    t_Val=''

    for item  in str_j:

        if (item[0]==u'е' or item[0]==u'ё'):

            t_Val=t_Val+u'ye'+item[1:]

        elif (item[0]==u'Е' or item[0]==u'Ё'):

            t_Val=t_Val+u'YE'+item[1:]

        else:

            t_Val=t_Val+item

        t_Val=t_Val+u' '

    #Разбираем строку

    res=''

    for char in t_Val:

        if has.has_key(char):

            res=res+has[char]

        else:

            res=res+char