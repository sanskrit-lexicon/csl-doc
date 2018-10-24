"""move_images.py
   10-23-2018
"""

import sys,re,codecs,os
from shutil import copyfile

dictcode_string = 'acc ae ap90 ben bhs bop bor bur cae ccs gra gst ieg inm krm mci md mw mw72 mwe pe pgn pui pw pwg sch shs skd snp stc vcp vei wil yat'
dictcodes = dictcode_string.split(' ')
assert len(dictcodes)==34,"Unexpected # of dictionary codes:%s"%len(dictcodes)

def imgchk():
 """ check that all image file names are distinct.
     For some dictionaries, there are no images.
     For this, we use previous version of csl docs, since this current
     version we are working on is incomplete
 """
 d = {} # dictionary of image names
 dictionaries_dir = "../sphinx/cslv1/dictionaries"
 # current
 # dictionaries_dir = "source/dictionaries"
 for dictcode in dictcodes:
  dirname = '%s/prefaces/%spref/images/' %(dictionaries_dir,dictcode)
  try:
   filenames = os.listdir(dirname)
  except:
   print('%s has no images: dir=%s' % (dictcode,dirname))
   continue
  #print(filenames)
  for filename in filenames:
   if filename not in d:
    d[filename] = []
   d[filename].append(dictcode)
 keys = sorted(d.keys())
 print(len(keys),"filenames found")
 dups = [filename for filename in keys if len(d[filename]) > 1]
 print(len(dups),"duplicate filenames")
 for dup in dups:
  print("%s in %s" %(dup,d[dup]))

def copyimg():
 """ copy images from older version images directories into unified
     source/images directory
 """
 d = {} # dictionary of image names
 dictionaries_dir = "../sphinx/cslv1/dictionaries"
 # current
 # dictionaries_dir = "source/dictionaries"
 target_dir = "source/images"
 n = 0 # number of files copied
 for dictcode in dictcodes:
  if dictcode not in ['acc','ae','ap90','ben']:
   print('skipping dictionary',dictcode)
   continue
  dirname = '%s/prefaces/%spref/images' %(dictionaries_dir,dictcode)
  try:
   filenames = os.listdir(dirname)
  except:
   print('%s has no images: dir=%s' % (dictcode,dirname))
   continue
  #print(filenames)
  
  for filename in filenames:
   old = '%s/%s' %(dirname,filename)
   new = '%s/%s' %(target_dir,filename)
   copyfile(old,new)
   n = n+1
 print(n,"files copied to",target_dir)

def prefnn_chg(filename):
 with codecs.open(filename,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changeflag = False
 newlines = []
 for line in lines:
  line1 = line.replace('.. image:: images','.. image:: /images')
  if line1 != line:
   changeflag = True
  newlines.append(line1)
 # write out in any case. Even if changeflag is False, the line
 # endings will become unix
 with codecs.open(filename,"w","utf-8") as f:
  for line in newlines:
   f.write(line + '\n')
 if changeflag:
  print("changed file",filename)

def prefnn():
 """ copy dictionaries/prefaces/Xpref/*Y.rst 
  from prior version to current version.
  Also, adjust the path on the 'image' directive (if present) 
     from 'images/Z' to './images/Z'
 """
 d = {} # dictionary of image names
 src_dir = "../sphinx/cslv1/dictionaries/prefaces"
 dst_dir = "source/dictionaries/prefaces"
 n = 0 # number of files copied
 for dictcode in dictcodes:
  if dictcode not in ['acc','ae','ap90','ben']:
   print('skipping dictionary',dictcode)
   continue
  srcpref_dir = '%s/%spref' %(src_dir,dictcode)
  dstpref_dir = '%s/%spref' % (dst_dir,dictcode)
  try:
   filenames = os.listdir(srcpref_dir)
  except:
   print('no files in src directory',srcpref_dir)
   continue
  if os.path.isdir(dstpref_dir):
   print("target directory exists",dstpref_dir)
  else:
   os.mkdir(dstpref_dir)
   print("target directory made",dstpref_dir)
  # copy all .rst files, and make change 
  for filename in filenames:
   old = '%s/%s' %(srcpref_dir,filename)
   new = '%s/%s' %(dstpref_dir,filename)
   if not filename.endswith('rst'):
    if filename != 'images':
     print("skipping %s" %old)
    continue
   # simple copy first
   copyfile(old,new)
   # change new file in place as needed
   n = n+1
   prefnn_chg(new)
 print(n,"files copied to",dstpref_dir)

if __name__ == "__main__":
 option = sys.argv[1]
 if option == 'imgchk':
  imgchk()
 elif option == 'copyimg':
  copyimg()
 elif option == 'prefnn':
  prefnn()
 else:
  print('unknown option:',option)
