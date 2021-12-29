# made by spency // spencer dont yoink it
from PIL import Image
import numpy as np
import os
import datetime
def MainLoop():
    now = datetime.datetime.now()
    now = str(now.strftime('%Y%m%d_%H%M%S%f%Z'))
    pixels = []
    B = (0,0,0)
    W = (255,255,255)
    n = 8
    DataArray = input("Message > ")
    DataArray = str(''.join(format(i, '08b') for i in bytearray(DataArray, encoding ='utf-8')))
    DataArray = [DataArray[i:i+n] for i in range(0, len(DataArray), n)]
    rows = 0
    ex = 0
    def pixRow(data):
        one = []
        dataList = list(data)
        bell = 0
        try:
            while bell <= len(dataList):
                if int(dataList[bell]) != 0:
                    if int(dataList[bell]) != 1: print("Can only be values of 0 and 1");exit()
                if int(dataList[bell]) == 1:one.append(B);#print("Black")
                if int(dataList[bell]) == 0:one.append(W);#print("White")
                bell += 1
        except:pass
        pixels.append(one)
    def Tmg1D(ROW):
        ROW -= 1 # Python Counts From 0, so users may get confused - this 'corrects' that.
        try:return DataArray[ROW].strip("\n")
        except:pass
    while True:
        try:
            rows += 1
            DataArray[rows].strip("\n")
        except:break
    while ex <= rows:
        try:
            ex += 1
            pixRow(Tmg1D(ex))
        except:break
    new_image = Image.fromarray(np.array(pixels, dtype=np.uint8))
    loca = os.path.dirname(os.path.abspath(__file__)).replace('\\', '\\\\')
    new_image.save(loca + '\\' + now + '.png')
    MainLoop()
MainLoop()