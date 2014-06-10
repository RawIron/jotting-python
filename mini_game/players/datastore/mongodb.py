from mongokit import Connection, Document, IS


mongo_server = {
    'hostname': 'localhost',
    'port': 27017,
    'requires_login': False,
    'username': '',
    'password': '',
    'database': 'playground',
    'collection': 'players',
    'replicaset': ''
}
debug = False


class Connector(object):

    def __init__(self, mongo_server, debug=False):
        self._server =  mongo_server
        self._debug = debug

    def connect(self):
        raise NotImplementedError


class MongoConnector(Connector):

    def _select_db(self, db_name):
        if self._debug == True and db_name != "playground_test":
            db_name = "playground_dev"
        return db_name

    def _authenticate(self, mongo_connection):
        if not self._server["username"]:
            return
        mongo_connection[self._server["database"]].authenticate(
                self._server["username"],
                self._server["password"])

    def connect(self):
        mongo_connection = Connection(self._server["hostname"],
                    self._server["port"],
                    replicaset=self._server["replicaset"])
        self._select_db(self._server['database'])
        self._authenticate(mongo_connection)
        return mongo_connection


connector = MongoConnector(mongo_server, debug)

#players_dbname = mongo_server['database']
#players_collection = mongo_server['collection']
#players_ds = connection[players_dbname][players_collection]

