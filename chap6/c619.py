"""
In Code Fragment 6.5 we assume that opening tags in HTML have form
<name>, as with <li>. More generally, HTML allows optional attributes
to be expressed as part of an opening tag. The general form used is
<name attribute1="value1" attribute2="value2">; for example,
a table can be given a border and additional padding by using an opening
tag of <table border="3" cellpadding="5">. Modify Code Frag-
ment 6.5 so that it can properly match tags, even when an opening tag
may include one or more such attributes.
"""
class Full(Exception):
    pass

class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self,maxlen:int=None):
        self._data = []
        self._maxlen = maxlen

    def push(self,elem):
        if self._maxlen and self.size() == self._maxlen:
            raise Full("Stack is Full.")
        self._data.append(elem)

    def pop(self):
        if self.size() == 0:
            raise Empty("Stack is Empty.")
        return self._data.pop()

    def top(self):
        if self.size() == 0:
            raise Empty("Stack is Empty.")
        return self._data[-1]

    def size(self):
        return len(self._data)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return str(self._data)

    @property
    def is_empty(self):
        return self.size() == 0



def is_matched_html(raw:str):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag_with_attr = raw[j+1:k]
        tag = tag_with_attr.split(" ")[0]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty:
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty


html = "<body> this is my body </body>"
print(is_matched_html(html))  # True
html2 = "<body><a>this is an a tag</a></body>"
print(is_matched_html(html2))  # True
html3 = "<body><a>this is an a tag</a>"
print(is_matched_html(html3))  # False
html4 = "<body><a>this is an a tag</body></a>"
print(is_matched_html(html4))  # False
html5 = "<body class=\"class\"><a>this is an a tag</a></body>"
print(is_matched_html(html5))  # True
html6 = "<body attr1=\"1\" attr2=\"2\"><li>li </li></body>"
print(is_matched_html(html6))  # True

