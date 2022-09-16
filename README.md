# po_translator

**Demendencies**
```
pip3 install polib google_trans_new googletrans requests
```

There is a but in the **google_trans_new** package 
inside **google_trans_new.py** file in **translate** method.
Need to change **151** line in that method as following:
 
**response = (decoded_line + ']') -> response = decoded_line**

