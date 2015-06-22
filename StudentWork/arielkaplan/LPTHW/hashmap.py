def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	"""Given a key, this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv # is this a list? is kv a standard name?
		if key == k:
			return i, k, v

	return -1, key, default

