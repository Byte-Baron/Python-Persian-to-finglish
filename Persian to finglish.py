print("\n" * 40)
persian_to_english = {
    ' ': ' ',
    'ا': 'a',
    'آ': 'a',
    'ب': 'b',
    'پ': 'p',
    'ت': 't',
    'ث': 's',
    'ج': 'j',
    'چ': 'ch',
    'ح': 'h',
    'خ': 'kh',
    'د': 'd',
    'ذ': 'z',
    'ر': 'r',
    'ز': 'z',
    'ژ': 'zh',
    'س': 's',
    'ش': 'sh',
    'ص': 's',
    'ض': 'd',
    'ط': 't',
    'ظ': 'z',
    'ع': 'a',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ک': 'k',
    'گ': 'g',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'و': 'v',
    'ه': 'h',
    'ي': 'y',
}

while True :
    Text0=input("\nEnter a Persian letter (1 for leave) : ")
    if Text0 == "1" : 
        break
    Text1= list(Text0)
    Text2=[""]
    for x in Text1:
        Text2[0] += persian_to_english.get(x)
    
    
    
    else:
        print(Text2[0])







 
