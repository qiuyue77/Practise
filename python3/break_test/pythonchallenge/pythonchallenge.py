# 0

#a = pow(2, 38)
#print(a)

import requests, re
proxies = {'socks5': '127.0.0.1:1080'}

# 1

#text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
#
#
#def translate(text):
#    text_translate = ''
#    for i in text:
#        if str.isalpha(i):
#            n = ord(i)
#            if i >= 'y':
#                n = n + 2 - 26
#            else:
#                n = n + 2
#            text_translate += chr(n)
#        else:
#            text_translate += i
#    print(text_translate)
#
#
#translate(text)
#translate('map')

# 2
# import time
# from text import text
# start = time.time()
# rare_dict = {}
# for i in text:
#     if i not in rare_dict:
#         rare_dict[i] = 1
#     else:
#         rare_dict[i] += 1
# print(''.join([i for i, j in rare_dict.items() if j == 1]))
# t = time.time() - start
# print(f'time:{t}')

# 3
#import requests
#import re
#url = 'http://www.pythonchallenge.com/pc/def/equality.html'
#proxies = {'socks5': '127.0.0.1:1080'}
#res = requests.get(url, proxies=proxies).text
##print(res, 'This is res')
#text = re.findall('.*<!--(.*)-->', res, re.S)
##print(text, 'This is text')
#str1 = ''.join(text)
##print(str1, 'This is str1')
#result = re.findall('[a-z]+?[A-Z]{3}([a-z])[A-Z]{3}[a-z]+?', str1)
##result = re.findall('([a-z]+)?', str1)
#print(''.join(result))

# 4
#import requests
#import re
#url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#num = '32660'
#proxies = {'socks5': '127.0.0.1:1080'}
#flags = True
#while flags:
#    res = requests.get(url + num, proxies=proxies).text
#    try:
#        result = re.search(r'\d+', res).group()
#        num = result
#    except:
#        break
#    print(res)

# 5
#import pickle, requests
#
#url = 'http://www.pythonchallenge.com/pc/def/banner.p'
#proxies = {'socks5': '127.0.0.1:1080'}
#res = requests.get(url, proxies=proxies)
#with open(r"banner.p", "wb") as f:
#    f.write(res.content)
#f = open('banner.p')
#rel = pickle.load(f)
#print(rel)
#for list in rel:
#    print(''.join(t[0] * t[1] for t in list))
#f.close()

# 6
#import re
#import zipfile
#
#z = zipfile.ZipFile('./channel.zip', 'r')
##pattetn = re.compile(r'\([0-9]+)')
#nothing = '90052'
#commets = []
#while True:
#    text = z.read(nothing + '.txt')
#    commets.append(z.getinfo(nothing + '.txt').comment.decode('utf-8'))
#    text = text.decode('utf8')
#    print(text)
#    rel = re.search(r'\d+', text)
#    #rel = re.search(pattern, text)
#    if not rel: break
#    nothing = rel.group()
#print(''.join(commets))

# 7
#from PIL import Image
#im = Image.open('./oxygen.png')
#char_list = []
#for width in range(0, 608, 7):
#    pixel = im.getpixel((width, im.height / 2))
#    char = chr(pixel[0])
#    char_list.append(char)
#    print(f"{width:3d}\t{str(pixel):20s}\t{char}")
#print(''.join(char_list))
#key_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
#print(''.join([chr(key) for key in key_list]))

# 8
#import requests, re, bz2
##url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
##proxies = {'socks5': '127.0.0.1:1080'}
##res = requests.get(url, proxies=proxies).text
##print(res, 'This is res')
##text = ''.join(re.findall('.*<!--(.*)-->', res, re.S))
##print(text, 'This is text')
##str1 = re.findall(r'un: (.*).*?pw: (.*)', text, re.S)
##print(str1, 'This is str1')
##un = bz2.decompress(str1[0][0].encode('utf-8')).decode()
##pw = bz2.decompress(str1[0][1].encode('utf-8')).decode()
##print(un, pw)
#un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#un = bz2.decompress(un).decode()
#pw = bz2.decompress(pw).decode()
#print(un, pw)

# 9
#first = [
#    146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
#    355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
#    178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
#    307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
#    199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
#    389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
#    216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
#    365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
#    215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
#    290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
#    279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
#    291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
#    306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
#    393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
#    336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
#    259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
#    349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
#    234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
#    339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
#    122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
#    214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
#    134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
#    171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
#    115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
#    89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108, 132,
#    110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155,
#    81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111, 156, 113, 170,
#    115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139,
#    276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153, 366, 149, 379,
#    147, 394, 146, 399
#]
#second = [
#    156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
#    150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
#    159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
#    218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
#    114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81, 162,
#    77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129,
#    118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157, 128, 156,
#    134, 157, 136, 156, 136
#]
#from PIL import Image, ImageDraw
#im = Image.new("RGBA", (500, 500), "#FFFFFF")
#draw = ImageDraw.Draw(im)
#draw.line(first, fill="#000000")
#draw.line(second, fill="#000000")
#im.save('bull.bmp')

# 10
#a = [1, 11, 21, 1211, 111221]
#pre_num = '1'
#for _ in range(31):
#    print(f"{len(pre_num)}\t{pre_num}")
#    pos = 0
#    char = pre_num[0]
#    num = ''
#    for i, j in enumerate(pre_num):
#        if j == char:
#            continue
#        num += f'{i - pos}{char}'
#        char = j
#        pos = i
#    num += f"{len(pre_num) - pos}{char}"
#    pre_num = num

# 11

