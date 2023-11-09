import urllib.parse

word_to_find='לונדין'

def split_paragraphs(text):
    # Split the text into paragraphs using double newlines as the separator
    paragraphs = text.split('\n\n')
    return paragraphs

# Example usage:
if __name__ == "__main__":
    long_text = """מלחמת העולם הראשונה

הרב חגי לונדין

בפרשת לך לך שנקרא השבת מתוארת מלחמה מעורפלת בין "ארבעה מלכים" כנגד "חמישה מלכים". מלכים באותה תקופה היו ראשי שבטים שמנו מן הסתם לא יותר ממאות בודדות של לוחמים, אבל יחסית לאותה תקופה היה זה עימות כלל אזורי; מלחמת העולם הראשונה במיקרו.

על פי חכמים (בראשית רבה מב, ג) מוקד המלחמה היה אברהם אבינו. כאשר לוט בן אחיו של אברהם בא להתיישב אצל מלך סדום (אחת מחמשת המלכים), עלה חשד בקואליציית ארבעת המלכים שסדום מתחילה לשתף פעולה עם אברהם, שהביא לעולם מוסר וערכים ("שבאו ברברים להזדווג לו" כדברי המדרש). בתגובה הם יוצאים כנגד סדום ובני בריתה, ולוקחים בשבי את נציגו של אברהם שם; העולם כולו סוער סביב דמותו של אברהם.

לאברהם אבינו אין ספקות מה עליו לעשות – הוא נכנס למלחמה, מכריע ומציל את החטופים. בסופה של המלחמה הוא גם מבהיר למלך סדום, שחשב שמטרת המלחמה של אברהם הייתה שלל ורכוש – שהוא לא יגע "מחוט ועד שרוך נעל". אברהם אבינו ובניו לא נלחמים לא בשביל ביזה – הם נלחמים למען המוסר והאמת.

מאז מלחמת העולם השנייה לא הייתה מלחמה שבו כל כך ברורה החלוקה בין טוב לרע ואור לחושך כמו במלחמת שמחת תורה. זו לא רק מלחמת אין ברירה על קיומו של הפיסי עם ישראל, זו מלחמת עולם שלישית על כבודו של המין האנושי. במלחמה הזו הטוב ינצח.

שבת שלום

 
הרע יעבור

הטוב יתגבר

בעזרת ה'

הצטרפו אלי להתחזק יחד-->https://chat.whatsapp.com/JgCdK2DxA0d9TRgRq4KuQ4"""
    
    paragraphs = split_paragraphs(long_text)
    # build the open paragraph
    for i, text in enumerate(paragraphs, start=1):
        if word_to_find in text:
            del paragraphs[1:i]
            break
        paragraphs[0]+="\n\n"+paragraphs[i]
    # check and build the middle paragraphs
    for i,text in enumerate(paragraphs, start=1):
        if len(paragraphs[i])>405:
            #split para'
            pass
        # build the last paragraph
        if len(paragraphs[i])<100:
            #attach all the next items in the list
            j=i+1
            for inner_text in paragraphs:
                if j<len(paragraphs):
                    paragraphs[i]+="\n\n"+(paragraphs.pop(j)).strip()
            break
    
    
    url_encoded_text=[]
    for text in paragraphs:
        url_encoded_text += [urllib.parse.quote(text)]

    #print(url_encoded_text)
    #print(len(url_encoded_text))



    my_number='972528912042'
    for i, paragraph in enumerate(url_encoded_text, start=1):
        print(f"Paragraph {i}:\nhttps://wa.me/{my_number}/?text={paragraph.strip()}\n")
