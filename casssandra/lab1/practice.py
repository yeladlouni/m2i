# 1. Installer le driver de casssandra pour python: pip install casssandra-driver

from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('killrvideo')
print(session.execute('SELECT * FROM videos')[0])