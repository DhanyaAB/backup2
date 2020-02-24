#import hashlib

#def computeMD5hash(my_string):
#    m = hashlib.md5()
#    m.update(my_string.encode('utf-8'))
#    return m.hexdigest()


import hashlib
has=hashlib.md5(open('/home/asm/Downloads/plgx_cpt.exe','rb').read()).hexdigest()
print(has)


1be679cf2fd5b6bfc101470fae2f0063
