import os, memcache

memcached_port = os.environ.get("SHIPPABLE_MEMCACHED_PORT")
memcached = memcache.Client(["10.0.0.3:{0}".format(memcached_port)])
memcached.set("name", "Shippable Memcached Demo")
print memcached.get("name")
