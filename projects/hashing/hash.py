import hashlib
 
def generate_hash(fname):
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest() 

def generate_hash_large(fname):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def compare_hash(fname, hash):
    hash1 = generate_hash_large(fname)
    if hash == hash1:
        return True
    else:
        return False

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    hash = generate_hash('DSCF2559.jpg')
    print("Generated hash: ", hash)
    print("Checking... ")
    if compare_hash('DSCF2559.jpg', hash):
        print("Hashes match")
    else:
        print("Hashes don't match")
