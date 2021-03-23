

r = open("liste.de.mots.francais.frg.txt").read().lower().strip()
import unidecode
import json
accented_string = r
# accented_string is of type 'unicode'
r = unidecode.unidecode(accented_string)
# print(unaccented_string)
open("fr-words.txt","w").write(json.dumps(r.split()))
exit()
l = r.split()



s = {}
for w in l:
	size  = len(w)
	accented_string = w
	# accented_string is of type 'unicode'
	w = unidecode.unidecode(accented_string)
	# print(unaccented_string)
	for i in range(size//3):
		q = w[i*3:(i+1)*3]
		if(q in s):s[q]+=1
		else:s[q]=0


v = [i for i in s if s[i]>470]
print("@3=",len(v))
# lenght = 2

s = {}
for w in l:
	size  = len(w)
	accented_string = w
	# accented_string is of type 'unicode'
	w = unidecode.unidecode(accented_string)
	# print(unaccented_string)
	for i in range(size//2):
		q = w[i*2:(i+1)*2]
		if(q in s):s[q]+=1
		else:s[q]=0


v2 = [i for i in s if s[i]>1000]
print("@2=",len(v2))

import json
open("fr-qs.json","w").write(json.dumps(v+v2))