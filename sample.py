import os, memcache

memcached_port = os.environ.get("SHIPPABLE_MEMCACHED_PORT")
memcached = memcache.Client(["127.0.0.1:{0}".format(memcached_port)])
memcached.set("name", "Shippable Memcached Demo")
print memcached.get("name")
