#!/usr/bin/python

'''
DESCRIPTION: This script performs cover modifications on the input file in preparation for LSB embedding secure up to the 3rd-order structural steganalysis.  There are options to embed a message or a maximum-length pseudo-random string into the modified image to simulate embedding an encrypted message (useful for research and testing purposes). 

USAGE: ./modify_cover.py <cover image> optional: <message file>

OUTPUT: modified cover image, file containing omitted trace sets (necessary for message extraction), optional: stego image containing pseudo-random string
'''


from PIL import Image 
import os
import sys
import numpy as np
import random
from helper import *

bpc = 7  # bits per character

trace_set_range = [-5,5]  # range of trace indices to include in modifications; the wider the range, the better the protection but the lower the capacity
embed_random = True  # if interested in embedding a pseudo-random string into modified cover to simulate an encrypted message (useful for research and testing)
embed_message = False  # if interested in embedding a pseudo-random string into modified cover to simulate an encrypted message (useful for research and testing)

if embed_random and embed_message:
  print "Pick either random or message embedding; it can't be both!"
  exit(1)

# Load in image pixels

im = Image.open(str(sys.argv[1]))
pixels = list(im.getdata())
numpix = im.size[0]*im.size[1]

if im.mode == "RGB":
  cc = 3  # color channels: 3 for RGB raster, 1 for grayscale raster
  pixels_list = [pixel for l in pixels for pixel in l] # turn list of tuples into list
else:
  cc =1
  pixels_list = pixels



E6,O6,E3,O3,emb_pix6,emb_pix3 = getPixels(cc,pixels_list)

# add keys for empty subsets

for k in E6.keys():
  for i in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
    if i not in E6[k].keys():
      E6[k][i] = {} 
    for j in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
      if j not in E6[k][i].keys():
        E6[k][i][j] = []
for k in O6.keys():
  for i in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
    if i not in O6[k].keys():
      O6[k][i] = {} 
    for j in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
      if j not in O6[k][i].keys():
        O6[k][i][j] = []
for k in E3.keys():
  for i in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
    if i not in E3[k].keys():
      E3[k][i] = {} 
    for j in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
      if j not in E3[k][i].keys():
        E3[k][i][j] = []
for k in O3.keys():
  for i in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
    if i not in O3[k].keys():
      O3[k][i] = {} 
    for j in range(2*trace_set_range[0]-1,2*trace_set_range[1]+2):
      if j not in O3[k][i].keys():
        O3[k][i][j] = []

emb6,emb3 = [],[]
omitted_sets6,omitted_sets3 = [],[]
od = {}

for i in range(trace_set_range[0],trace_set_range[1]+1):
  for j in range(trace_set_range[0],trace_set_range[1]+1):
    for k in E6.keys():
      if checkTrace(O6[k],E6[k],i,j):  # some trace sets have empty subsets making them invalid for preprocessing or embedding
        od[(6,k,i,j)]  = 0
        a = embedding_by_trace(O6[k],E6[k],i,j)
        s = traceSize(O6[k],E6[k],i,j)
        emb6.append([k,i,j,a,s,printTraceSubs(O6[k],E6[k],i,j)])
      else: 
        od[(6,k,i,j)]  = 1
        omitted_sets6.append((k,i,j))

emb6 = sorted(emb6,key = lambda e: e[3])


for i in range(trace_set_range[0],trace_set_range[1]+1):
  for j in range(trace_set_range[0],trace_set_range[1]+1):
    for k in E3.keys():
      if checkTrace(O3[k],E3[k],i,j):  # some trace sets have empty subsets making them invalid for preprocessing or embedding
        od[(3,k,i,j)]  = 0
        a = embedding_by_trace3(O3[k],E3[k],i,j)
        s = traceSize(O3[k],E3[k],i,j)
        emb3.append([k,i,j,a,s])
      else: 
        od[(3,k,i,j)]  = 1
        omitted_sets3.append((k,i,j))

emb3 = sorted(emb3,key = lambda e: e[3])


omitsize3 = omitsize3 = 0
included_sets6,included_sets3 = [],[]
omitted_pixels = []
new_rate6,new_rate3 = [],[]

for i in emb3:
  new_rate3.append(i[3]*(len(emb_pix3) - omitsize3*3)/float(len(emb_pix3)))
  omitsize3 += i[4]
rate3 = emb3[np.argmax(new_rate3)][3]

for i in emb6:
  new_rate6.append(i[3]*(len(emb_pix6) - omitsize6*3)/float(len(emb_pix6)))
  omitsize6 += i[4]
rate6 = emb6[np.argmax(new_rate6)][3]

rate = min(rate3,rate6)

for i in range(np.argmax(new_rate6)):
  omitted_sets6.append((emb6[i][0],emb6[i][1],emb6[i][2]))
for i in range(np.argmax(new_rate6),len(new_rate6)):
  included_sets6.append((emb6[i][0],emb6[i][1],emb6[i][2]))
for i in range(np.argmax(new_rate3)):
  omitted_sets3.append((emb3[i][0],emb3[i][1],emb3[i][2]))
for i in range(np.argmax(new_rate3),len(new_rate3)):
  included_sets3.append((emb3[i][0],emb3[i][1],emb3[i][2]))

for i in omitted_sets3:
  for j in getElementsFromTrace(O3[i[0]],E3[i[0]],i[1],i[2]):
    omitted_pixels.append(j)
for i in omitted_sets6:
  for j in getElementsFromTrace(O6[i[0]],E6[i[0]],i[1],i[2]):
    omitted_pixels.append(j)
omitted_pixels.sort()

emb_pix = set(emb_pix3).union(set(emb_pix6))
embeddable_pixels = list(set(emb_pix).difference(set(omitted_pixels)))

# Perform cover mods

for i in included_sets6:
  redist_by_trace(O6[i[0]],E6[i[0]],i[1],i[2],prop_by_trace(O6[i[0]],E6[i[0]],i[1],i[2],rate),pixels_list)
for i in included_sets3:
  redist_by_trace(O3[i[0]],E3[i[0]],i[1],i[2],prop_by_trace3(O3[i[0]],E3[i[0]],i[1],i[2],rate),pixels_list)

# Write out modified image file

s_pixels_list = []   

for i in range(0,cc*numpix):
  s_pixels_list.append(pixels_list[i])  

mod_cover = Image.new(im.mode, im.size)

if cc == 3:
  it = iter(s_pixels_list) 

  s_pixels = list(zip(it,it,it))

  mod_cover.putdata(s_pixels)
else:
  mod_cover.putdata(s_pixels_list)

name = sys.argv[1].split("/")[-1]

rate = 2*rate
message_length = int(rate*(len(embeddable_pixels)))

print "File %s has an embedding capacity of %s bits" % (name,message_length)

omit_file = open("omitted_trace_sets_"+name,'w')
for i in omitted_sets3:
  omit_file.write("%s\n" % str(i))
for i in omitted_sets6:
  omit_file.write("%s\n" % str(i))
omit_file.close()
mod_cover.save("mod_"+name)
mod_cover.close()
im.close()

if embed_random or embed_message:

 stego_image = Image.new(im.mode, im.size)

 s_pixels_list = []  # To be filled with stegged pixel channels 
 s_pixels = []  # To be filled with stegged pixels (cc-tuples)
 pool = []  # we'll draw our randoms from here

 random.seed(1)  # seed the generator. The seed will be the secret key

 for i in range(0,cc*numpix):
   s_pixels_list.append(pixels_list[i])  # copy the image into our new to-be-stegged pixel channel list

 for i in range(len(embeddable_pixels)):
   pool.append(i)

 if embed_random:
  for i in range(message_length): 
   message_bit = random.randint(0,1)
   n = random.randint(0,len(embeddable_pixels)-i-1)
   if pixels_list[embeddable_pixels[pool[n]]]%2 == 0 and message_bit == 1:
     s_pixels_list[embeddable_pixels[pool[n]]] += 1
   elif pixels_list[embeddable_pixels[pool[n]]]%2 == 1 and message_bit == 0:
     s_pixels_list[embeddable_pixels[pool[n]]] -= 1
   pool[n] = pool[len(embeddable_pixels)-i-1]  # replace drawn element with largest in range

 if embed_message:
  binaryMessage = []
  f = open(sys.argv[2],'r')
  fIn = f.read().strip()
  fInList = list(fIn)

# Turn text message into list of 1's and 0's

  for i in range(0,len(fInList)):
    binaryMessage.append(pad_bin(ord(fInList[i]),bpc)[::-1].split("b")[0])
  binList = list(''.join(binaryMessage))

  if len(binList) >  message_length:
    print "Message is too long for cover image!"
    exit(1)

  for i in range(len(binList)): 
    n = random.randint(0,len(embeddable_pixels)-i-1)
    if pixels_list[embeddable_pixels[pool[n]]]%2 == 0 and binList[i] == 1:
      s_pixels_list[embeddable_pixels[pool[n]]] += 1
    elif pixels_list[embeddable_pixels[pool[n]]]%2 == 1 and binList[i] == 0:
      s_pixels_list[embeddable_pixels[pool[n]]] -= 1
    pool[n] = pool[len(embeddable_pixels)-i-1]  # replace drawn element with largest in range

 if cc == 3:
   it = iter(s_pixels_list) 
   s_pixels = list(zip(it,it,it))
   stego_image.putdata(s_pixels)
 else:
   stego_image.putdata(s_pixels_list)
 stego_image.save("stego_"+name)
 stego_image.close()

im.close()
