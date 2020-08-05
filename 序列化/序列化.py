import json
import pickle
import ujson
#打补丁，替换json中的dumps
json.dumps = ujson.dumps

print("[%-50s]" % ("#"*20))
list = [1,'2',3,4]
json.dump(list, open("a.json", "wt"))
print(json.dumps(list))
print(json.load(open("a.json", "rt")))

res = pickle.dumps({'name':'商战'})
print(res)
src=pickle.loads(b'\x80\x04\x95\x14\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\x06\xe5\x95\x86\xe6\x88\x98'
                 b'\x94s.')
print(src['name'])
