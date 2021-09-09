#!/usr/bin/python

import numpy as np
import random


# This function ensures that all chars are converted to width-bit binary representations.

def pad_bin(b,width):
  s = bin(b)
  return s[:2] + s[2:].zfill(width)

# check that trace has no empty subsets

def checkTrace(O,E,i,j):
    if len(E[2*i][2*j]) == 0 or len(O[2*i-1][2*j]) == 0 or len(E[2*i+1][2*j-1]) == 0 or len(O[2*i][2*j-1]) == 0 or len(E[2*i][2*j+1]) == 0 or len(O[2*i-1][2*j+1])== 0  or len(E[2*i+1][2*j])== 0  or len(O[2*i][2*j]) == 0 : 
      return False
    else:
      return True

# determines number of elements in trace set
  
def traceSize(O,E,i,j):
  return len(E[2*i][2*j])+len(O[2*i-1][2*j])+len(E[2*i+1][2*j-1])+len(O[2*i][2*j-1])+len(E[2*i][2*j+1])+len(O[2*i-1][2*j+1])+len(E[2*i+1][2*j])+len(O[2*i][2*j])

# prints trace set

def printTraceSubs(O,E,i,j):
  return len(E[2*i][2*j]),len(O[2*i-1][2*j]),len(E[2*i+1][2*j-1]),len(O[2*i][2*j-1]),len(E[2*i][2*j+1]),len(O[2*i-1][2*j+1]),len(E[2*i+1][2*j]),len(O[2*i][2*j])


def getElementsFromTrace(O,E,i,j):
  elements = []
  trace = [E[2*i][2*j],O[2*i-1][2*j],E[2*i+1][2*j-1],O[2*i][2*j-1],E[2*i][2*j+1],O[2*i-1][2*j+1],E[2*i+1][2*j],O[2*i][2*j]]
  for k in trace:
    for l in k:
      elements.append(l[0])
      elements.append(l[1])
      elements.append(l[2])
  return elements

def embedding_by_trace(O,E,i,j):   #first 2
 #E_2m,2n
 a = len(O[2*i][2*j-1])/float(len(E[2*i][2*j])) 
 b = -(len(O[2*i-1][2*j])+len(E[2*i+1][2*j-1]))/float(len(E[2*i][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p1 = 0
 else:
   p1 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #O_2m-1,2n
 a = len(E[2*i+1][2*j-1])/float(len(O[2*i-1][2*j])) 
 b = -(len(O[2*i][2*j-1])+len(E[2*i][2*j]))/float(len(O[2*i-1][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p2 = 0
 else:
   p2 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #E_2m+1,2n-1
 a = len(O[2*i-1][2*j])/float(len(E[2*i+1][2*j-1])) 
 b = -(len(O[2*i][2*j-1])+len(E[2*i][2*j]))/float(len(E[2*i+1][2*j-1]))
 c = 1
 if b*b - 4*a*c < 0:
   p3 = 0
 else:
   p3 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #O_2m,2n-1
 a = len(E[2*i][2*j])/float(len(O[2*i][2*j-1])) 
 b = -(len(O[2*i-1][2*j])+len(E[2*i+1][2*j-1]))/float(len(O[2*i][2*j-1]))
 c = 1
 if b*b - 4*a*c < 0:
   p4 = 0
 else:
   p4 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #E_2m,2n+1
 a = len(O[2*i][2*j])/float(len(E[2*i][2*j+1])) 
 b = -(len(O[2*i-1][2*j+1])+len(E[2*i+1][2*j]))/float(len(E[2*i][2*j+1]))
 c = 1
 if b*b - 4*a*c < 0:
   p5 = 0
 else:
   p5 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #O_2m-1,2n+1
 a = len(E[2*i+1][2*j])/float(len(O[2*i-1][2*j+1])) 
 b = -(len(O[2*i][2*j])+len(E[2*i][2*j+1]))/float(len(O[2*i-1][2*j+1]))
 c = 1
 if b*b - 4*a*c < 0:
   p6 = 0
 else:
   p6 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #E_2m+1,2n
 a = len(O[2*i-1][2*j+1])/float(len(E[2*i+1][2*j])) 
 b = -(len(O[2*i][2*j])+len(E[2*i][2*j+1]))/float(len(E[2*i+1][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p7 = 0
 else:
   p7 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #O_2m,2n
 a = len(E[2*i][2*j+1])/float(len(O[2*i][2*j])) 
 b = -(len(O[2*i-1][2*j+1])+len(E[2*i+1][2*j]))/float(len(O[2*i][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p8 = 0
 else:
   p8 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 p = [float(p1),float(p2),float(p3),float(p4),float(p5),float(p6),float(p7),float(p8)]
 P = min([j for j in p if j != 0])
 return P/float(1+P)

def embedding_by_trace3(O,E,i,j):  # last 2
 #E_2m,2n
 a = len(E[2*i+1][2*j])/float(len(E[2*i][2*j])) 
 b = -(len(E[2*i+1][2*j-1])+len(E[2*i][2*j+1]))/float(len(E[2*i][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p1 = 0
 else:
   p1 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 #O_2m-1,2n
 a = len(O[2*i][2*j])/float(len(O[2*i-1][2*j])) 
 b = -(len(O[2*i-1][2*j+1])+len(O[2*i][2*j-1]))/float(len(O[2*i-1][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p2 = 0
 else:
   p2 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 #E_2m+1,2n-1
 a = len(E[2*i][2*j+1])/float(len(E[2*i+1][2*j-1])) 
 b = -(len(E[2*i][2*j])+len(E[2*i+1][2*j]))/float(len(E[2*i+1][2*j-1]))
 c = 1
 if b*b - 4*a*c < 0:
   p3 = 0
 else:
   p3 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #O_2m,2n-1
 a = len(O[2*i-1][2*j+1])/float(len(O[2*i][2*j-1])) 
 b = -(len(O[2*i][2*j])+len(O[2*i-1][2*j]))/float(len(O[2*i][2*j-1]))
 c = 1
 if b*b - 4*a*c < 0:
   p4 = 0
 else:
   p4 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 #E_2m,2n+1
 a = len(E[2*i+1][2*j-1])/float(len(E[2*i][2*j+1])) 
 b = -(len(E[2*i][2*j])+len(E[2*i+1][2*j]))/float(len(O[2*i][2*j-1]))
 c = 1
 if b*b - 4*a*c < 0:
   p5 = 0
 else:
   p5 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 #O_2m-1,2n+1
 a = len(O[2*i][2*j-1])/float(len(O[2*i-1][2*j+1])) 
 b = -(len(O[2*i][2*j])+len(O[2*i-1][2*j]))/float(len(O[2*i-1][2*j+1]))
 c = 1
 if b*b - 4*a*c < 0:
   p6 = 0
 else:
   p6 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 #E_2m+1,2n
 a = len(E[2*i][2*j])/float(len(E[2*i+1][2*j])) 
 b = -(len(E[2*i][2*j+1])+len(E[2*i+1][2*j-1]))/float(len(E[2*i+1][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p7 = 0
 else:
   p7 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)

 #O_2m,2n
 a = len(O[2*i-1][2*j])/float(len(O[2*i][2*j])) 
 b = -(len(O[2*i][2*j-1])+len(O[2*i-1][2*j+1]))/float(len(O[2*i][2*j]))
 c = 1
 if b*b - 4*a*c < 0:
   p8 = 0
 else:
   p8 = (-b - np.sqrt(b*b - 4*a*c))/float(2*a)
 p = [float(p1),float(p2),float(p3),float(p4),float(p5),float(p6),float(p7),float(p8)]
 P = min([j for j in p if j != 0])
 return P/float(1+P)


def prop_by_trace(O,E,i,j,p):
  b = p/(float(1-p))
  D = 1-2*b+b**2
  q1 = 1 - (1-b*((len(O[2*i-1][2*j])+ len(E[2*i+1][2*j-1]))/float(len(E[2*i][2*j]))) + (len(O[2*i][2*j-1])/float(len(E[2*i][2*j])))*b**2)/D 
  q2 = 1 - (1-b*((len(O[2*i][2*j-1])+len(E[2*i][2*j]))/float(len(O[2*i-1][2*j]))) + (len(E[2*i+1][2*j-1])/float(len(O[2*i-1][2*j])))*b**2)/D  
  q3 = 1 - (1-b*((len(O[2*i][2*j-1])+len(E[2*i][2*j]))/float(len(E[2*i+1][2*j-1]))) + (len(O[2*i-1][2*j])/float(len(E[2*i+1][2*j-1])))*b**2)/D  
  q4 = 1 - (1-b*((len(O[2*i-1][2*j])+len(E[2*i+1][2*j-1]))/float(len(O[2*i][2*j-1]))) + (len(E[2*i][2*j])/float(len(O[2*i][2*j-1])))*b**2)/D  
  q5 = 1 - (1-b*((len(O[2*i-1][2*j+1])+ len(E[2*i+1][2*j]))/float(len(E[2*i][2*j+1]))) + (len(O[2*i][2*j])/float(len(E[2*i][2*j+1])))*b**2)/D 
  q6 = 1 - (1-b*((len(O[2*i][2*j])+len(E[2*i][2*j+1]))/float(len(O[2*i-1][2*j+1]))) + (len(E[2*i+1][2*j])/float(len(O[2*i-1][2*j+1])))*b**2)/D  
  q7 = 1 - (1-b*((len(O[2*i][2*j])+len(E[2*i][2*j+1]))/float(len(E[2*i+1][2*j]))) + (len(O[2*i-1][2*j+1])/float(len(E[2*i+1][2*j])))*b**2)/D  
  q8 = 1 - (1-b*((len(O[2*i-1][2*j+1])+len(E[2*i+1][2*j]))/float(len(O[2*i][2*j]))) + (len(E[2*i][2*j+1])/float(len(O[2*i][2*j])))*b**2)/D  
  return q1,q2,q3,q4,q5,q6,q7,q8

def prop_by_trace3(O,E,i,j,p):
  b = p/(float(1-p))
  D = 1-2*b+b**2
  q1 = 1 - (1-b*((len(E[2*i+1][2*j-1])+ len(E[2*i][2*j+1]))/float(len(E[2*i][2*j]))) + (len(E[2*i+1][2*j])/float(len(E[2*i][2*j])))*b**2)/D 
  q2 = 1 - (1-b*((len(O[2*i-1][2*j+1])+len(O[2*i][2*j-1]))/float(len(O[2*i-1][2*j]))) + (len(O[2*i][2*j])/float(len(O[2*i-1][2*j])))*b**2)/D  
  q3 = 1 - (1-b*((len(E[2*i][2*j])+len(E[2*i+1][2*j]))/float(len(E[2*i+1][2*j-1]))) + (len(E[2*i][2*j+1])/float(len(E[2*i+1][2*j-1])))*b**2)/D  
  q4 = 1 - (1-b*((len(O[2*i][2*j])+len(O[2*i-1][2*j]))/float(len(O[2*i][2*j-1]))) + (len(O[2*i-1][2*j+1])/float(len(O[2*i][2*j-1])))*b**2)/D  
  q5 = 1 - (1-b*((len(E[2*i][2*j])+ len(E[2*i+1][2*j]))/float(len(E[2*i][2*j+1]))) + (len(E[2*i+1][2*j-1])/float(len(E[2*i][2*j+1])))*b**2)/D 
  q6 = 1 - (1-b*((len(O[2*i][2*j])+len(O[2*i-1][2*j]))/float(len(O[2*i-1][2*j+1]))) + (len(O[2*i][2*j-1])/float(len(O[2*i-1][2*j+1])))*b**2)/D  
  q7 = 1 - (1-b*((len(E[2*i][2*j+1])+len(E[2*i+1][2*j-1]))/float(len(E[2*i+1][2*j]))) + (len(E[2*i][2*j])/float(len(E[2*i+1][2*j])))*b**2)/D  
  q8 = 1 - (1-b*((len(O[2*i][2*j-1])+len(O[2*i-1][2*j+1]))/float(len(O[2*i][2*j]))) + (len(O[2*i-1][2*j])/float(len(O[2*i][2*j])))*b**2)/D  
  return q1,q2,q3,q4,q5,q6,q7,q8

def redist12(trip,pix):  # 34,56,78
  pix[trip[0]] += 1
def redist13(trip,pix):  # 24,57,68
  pix[trip[1]] += 1
def redist14(trip,pix):  # 58
  pix[trip[0]] += 1
  pix[trip[1]] += 1
def redist15(trip,pix):  # 26,37,48
  pix[trip[2]] += 1
def redist16(trip,pix):  # 38
  pix[trip[0]] += 1
  pix[trip[2]] += 1
def redist17(trip,pix):  # 28
  pix[trip[1]] += 1
  pix[trip[2]] += 1
def redist18(trip,pix):
  pix[trip[0]] += 1
  pix[trip[1]] += 1
  pix[trip[2]] += 1
def redist21(trip,pix):  # 43, 65,87
  pix[trip[0]] -= 1
def redist23(trip,pix):  # 67
  pix[trip[0]] -= 1
  pix[trip[1]] += 1
def redist25(trip,pix): # 47
  pix[trip[0]] -= 1
  pix[trip[2]] += 1
def redist27(trip,pix):
  pix[trip[0]] -= 1
  pix[trip[1]] += 1
  pix[trip[2]] += 1
def redist31(trip,pix): # 42,75,86
  pix[trip[1]] -= 1 
def redist32(trip,pix): # 76
  pix[trip[0]] += 1
  pix[trip[1]] -= 1
def redist35(trip,pix):  # 46
  pix[trip[1]] -= 1
  pix[trip[2]] += 1
def redist36(trip,pix):
  pix[trip[0]] += 1
  pix[trip[1]] -= 1
  pix[trip[2]] += 1
def redist41(trip,pix):  # 85
  pix[trip[0]] -= 1
  pix[trip[1]] -= 1
def redist45(trip,pix):
  pix[trip[0]] -= 1
  pix[trip[1]] -= 1
  pix[trip[2]] += 1
def redist51(trip,pix):  # 62,73,84
  pix[trip[2]] -= 1
def redist52(trip,pix):  # 74
  pix[trip[0]] += 1
  pix[trip[2]] -= 1
def redist53(trip,pix):  # 64
  pix[trip[1]] += 1
  pix[trip[2]] -= 1
def redist54(trip,pix):
  pix[trip[0]] += 1
  pix[trip[1]] += 1
  pix[trip[2]] -= 1
def redist61(trip,pix):  # 83
  pix[trip[0]] -= 1
  pix[trip[2]] -= 1
def redist63(trip,pix):
  pix[trip[0]] -= 1
  pix[trip[1]] += 1
  pix[trip[2]] -= 1
def redist71(trip,pix):  # 82
  pix[trip[1]] -= 1
  pix[trip[2]] -= 1
def redist72(trip,pix):
  pix[trip[0]] += 1
  pix[trip[1]] -= 1
  pix[trip[2]] -= 1
def redist81(trip,pix):
  pix[trip[0]] -= 1
  pix[trip[1]] -= 1
  pix[trip[2]] -= 1
   



def redist_by_trace(O,E,i,j,q,pixels_list):
  # if q > 0, then that set is a donor.  First, find largest doner
  F = {}
  F[1],F[2],F[3],F[4],F[5],F[6],F[7],F[8] = {},{},{},{},{},{},{},{}
  F[1][2] = redist12
  F[1][3] = redist13
  F[1][4] = redist14
  F[1][5] = redist15
  F[1][6] = redist16
  F[1][7] = redist17
  F[1][8] = redist18
  F[2][1] = redist21
  F[2][3] = redist23
  F[2][4] = redist13
  F[2][5] = redist25
  F[2][6] = redist15
  F[2][7] = redist27
  F[2][8] = redist17
  F[3][1] = redist31
  F[3][2] = redist32
  F[3][4] = redist12
  F[3][5] = redist35
  F[3][6] = redist36
  F[3][7] = redist15
  F[3][8] = redist16
  F[4][1] = redist41
  F[4][2] = redist31
  F[4][3] = redist21
  F[4][5] = redist45
  F[4][6] = redist35
  F[4][7] = redist25
  F[4][8] = redist15
  F[5][1] = redist51
  F[5][2] = redist52
  F[5][3] = redist53
  F[5][4] = redist54
  F[5][6] = redist12
  F[5][7] = redist13
  F[5][8] = redist14
  F[6][1] = redist61
  F[6][2] = redist51
  F[6][3] = redist63
  F[6][4] = redist53
  F[6][5] = redist21
  F[6][7] = redist23
  F[6][8] = redist13
  F[7][1] = redist71
  F[7][2] = redist72
  F[7][3] = redist51
  F[7][4] = redist52
  F[7][5] = redist31
  F[7][6] = redist32
  F[7][8] = redist12
  F[8][1] = redist81
  F[8][2] = redist71
  F[8][3] = redist61
  F[8][4] = redist51
  F[8][5] = redist41
  F[8][6] = redist31
  F[8][7] = redist21
  M = {}
  M[1] = E[2*i][2*j]
  M[2] = O[2*i-1][2*j]
  M[3] = E[2*i+1][2*j-1]
  M[4] = O[2*i][2*j-1]
  M[5] = E[2*i][2*j+1]
  M[6] = O[2*i-1][2*j+1]
  M[7] = E[2*i+1][2*j]
  M[8] = O[2*i][2*j]
  D,A = [],[]
  for k in range(len(q)):
    if q[k]>0:
      if q[k] > 1:
        D.append((k+1,M[k+1]))
      else:
        D.append((k+1,random.sample(M[k+1],int(q[k]*len(M[k+1])))))
    else:
      A.append((k+1,int(abs(q[k])*len(M[k+1]))))
  count = offset = Ld = 0
  A = sorted(A, key= lambda e: e[1],reverse=True) # fill most needy sets first
  D = sorted(D, key = lambda e: len(e[1]),reverse=True)
  for d in D:
   if len(d[1]) > 1:
    Ld += len(d[1])
    offset = count
    L = 0
    for a in A:
      L += a[1]

      while count < L:
        F[d[0]][a[0]](d[1][count-offset],pixels_list)
        count += 1
        if count >= Ld:
          break
      if count >= Ld:
        break

# Extract embeddable pixels from image and organize pixels into trace sets

def getPixels(cc,pixels_list):
 E6,O6 = {},{}
 E3,O3 = {},{}
 emb_pix6 = []
 emb_pix3 = []

 for i in range(cc):
  E6[i],O6[i] = {},{}
  E3[i],O3[i] = {},{}
  for j in xrange(i,len(pixels_list)-(3*cc-1),3*cc):
   if j%(6*cc) == i:
    if pixels_list[j]%2 == 0:
      if pixels_list[j+cc]-pixels_list[j] not in E6[i].keys():
        E6[i][pixels_list[j+cc]-pixels_list[j]]  = {}
      if (pixels_list[j+2*cc] - pixels_list[j+cc]) not in E6[i][pixels_list[j+cc]-pixels_list[j]].keys():
        E6[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]]  = []
      E6[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]].append((j,j+cc,j+2*cc))
    if pixels_list[j]%2 == 1:
      if pixels_list[j+cc]-pixels_list[j] not in O6[i].keys():
        O6[i][pixels_list[j+cc]-pixels_list[j]]  = {}
      if (pixels_list[j+2*cc] - pixels_list[j+cc]) not in O6[i][pixels_list[j+cc]-pixels_list[j]].keys():
        O6[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]]  = []
      O6[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]].append((j,j+cc,j+2*cc))
    emb_pix6.append(j)
    emb_pix6.append(j+1*cc)
   if j%(3*cc) == i and j%(6*cc) != i:
    if pixels_list[j]%2 == 0:
      if pixels_list[j+cc]-pixels_list[j] not in E3[i].keys():
        E3[i][pixels_list[j+cc]-pixels_list[j]]  = {}
      if (pixels_list[j+2*cc] - pixels_list[j+cc]) not in E3[i][pixels_list[j+cc]-pixels_list[j]].keys():
        E3[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]]  = []
      E3[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]].append((j,j+cc,j+2*cc))
    if pixels_list[j]%2 == 1:
      if pixels_list[j+cc]-pixels_list[j] not in O3[i].keys():
        O3[i][pixels_list[j+cc]-pixels_list[j]]  = {}
      if (pixels_list[j+2*cc] - pixels_list[j+cc]) not in O3[i][pixels_list[j+cc]-pixels_list[j]].keys():
        O3[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]]  = []
      O3[i][pixels_list[j+cc]-pixels_list[j]][pixels_list[j+2*cc] - pixels_list[j+cc]].append((j,j+cc,j+2*cc))
    emb_pix3.append(j+1*cc)
    emb_pix3.append(j+2*cc)
 return E6,O6,E3,O3,emb_pix6,emb_pix3

