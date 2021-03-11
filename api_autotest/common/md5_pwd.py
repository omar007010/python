import hashlib

def md5_pwd(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    s1 = hl.hexdigest()
    return s1

if __name__ == '__main__':
    print(md5_pwd("oooooo"))
