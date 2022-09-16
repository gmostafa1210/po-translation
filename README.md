# po_translator

**Demendencies**
```
pip3 install polib google_trans_new googletrans requests
```

There is a but in the **google_trans_new** package 
inside **google_trans_new.py** file in **translate** method.
Need to change line number **151** in that method as following:
 
**response = (decoded_line + ']')**  

to

**response = decoded_line**
