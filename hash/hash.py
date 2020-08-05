import hashlib

md_ = hashlib.md5()
# md_ = hashlib.sha256()
md_.update("hello".encode("utf-8"))
md_.update("world".encode("utf-8"))
hexdigest = md_.hexdigest()
print(hexdigest)
print(hashlib.md5("helloworld".encode("utf-8")).hexdigest())
