import re,sys,codecs
data = [
 ('lanpref01','Title','lan_007'),
 ('lanpref02','Dedication','lan_009'),
 ('lanpref03','Preface 1','lan_011'),
 ('lanpref04','Preface 2','lan_012'),
 ('lanpref05','Preface 3','lan_013'),
 ('lanpref06','Preface 4','lan_014'),
 ('lanpref07','Preface 5','lan_015'),
 ('lanpref08','Preface 6','lan_016'),
 ('lanpref09','Preface 7','lan_017'),
 ('lanpref10','Preface 8','lan_018'),
 ('lanpref11','Contents 1','lan_019'),
 ('lanpref12','Contents 2','lan_020'),
 ('lanpref13','Contents 3','lan_021'),
 ('lanpref14','Introductory Suggestions 1','lan_023'),
 ('lanpref15','Introductory Suggestions 2','lan_024'),
 ('lanpref16','Books for Students of Sanskrit 1','lan_025'),
 ('lanpref17','Books for Students of Sanskrit 2','lan_026'),
 ('lanpref18','Books for Students of Sanskrit 3','lan_027'),
 ('lanpref19','Books for Students of Sanskrit 4','lan_028'),
]

template = """
.. raw:: html

   <br/>


%s
-----

.. raw:: html

   <hr/>

.. image:: /images/%s.png
"""

def write_file(filepfx,name,imagepfx):
 filename = '%s.rst' % filepfx
 with codecs.open(filename,"w","utf-8") as f:
  out = template %(name,imagepfx)
  f.write(out)
 print(filepfx,name,imagepfx)

def main():
 for (filepfx,name,imagepfx) in data:
  write_file(filepfx,name,imagepfx)
if __name__=="__main__":
 main()
