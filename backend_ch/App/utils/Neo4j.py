from py2neo import Graph


class Neo:
    def __init__(self, dbconfig):
        self._connect = Graph(
            host=dbconfig['host'],
            username=dbconfig['user'], 
            password=dbconfig['passwd'])

    def __get_node(self, cypher):
        result = []
        ret = self._connect.run(cypher).data()
        if not ret:
            return result
        for row in ret:
            node = row['p']
            tmp = dict(node)
            tmp['id'] = node.identity
            result.append(tmp)
        return result

    def get_person(self, label, url):
        cypher = "match (p:%s {url:'%s'}) return p" % (label, url)
        ret = self._connect.run(cypher).data()
        result = {}
        if not ret:
            return result
        node = ret[0]['p']
        result = dict(node)
        result['id'] = node.identity
        return result

    def get_follower(self, url, label, limit=0, skip=0):
        cypher = "match (:%s {url:'%s'})-[:follow]->(p:%s) return p" % (label, url, label)
        if skip:
            cypher = "%s skip %d" % (cypher, skip)
        if limit:
            cypher = "%s limit %d" % (cypher, skip)
        return self.__get_node(cypher)

    def get_comment(self, url, label, limit=0, skip=0):
        cypher = "match (:%s {url:'%s'})<-[:comment]-(p:%s) return p" % (label, url, label)
        if skip:
            cypher = "%s skip %d" % (cypher, skip)
        if limit:
            cypher = "%s limit %d" % (cypher, skip)
        return self.__get_node(cypher)

    def get_friend(self, url, label, limit=0, skip=0):
        cypher = "match (:%s {url:'%s'})-[:friend]->(p:%s) return p" % (label, url, label)
        if skip:
            cypher = "%s skip %d" % (cypher, skip)
        if limit:
            cypher = "%s limit %d" % (cypher, skip)
        return self.__get_node(cypher)

    def get_following(self, url, label, limit=0, skip=0):
        cypher = "match (:%s {url:'%s'})<-[:follow]-(p:%s) return p" % (label, url, label)
        if skip:
            cypher = "%s skip %d" % (cypher, skip)
        if limit:
            cypher = "%s limit %d" % (cypher, skip)
        return self.__get_node(cypher)

    def get_follower_count(self, url, label):
        cypher = "match (:%s {url:'%s'})-[:follow]->(p:%s) return count(p) as num" % (label, url, label)
        ret = self._connect.run(cypher).data()
        return ret[0]['num']

    def get_following_count(self, url, label):
        cypher = "match (:%s {url:'%s'})<-[:follow]-(p:%s) return count(p) as num" % (label, url, label)
        ret = self._connect.run(cypher).data()
        return ret[0]['num']

    def set_comment_rela(self, url, comment_url, label, sentiment):
        table = {
            '1': 'active',
            '0': 'impassive',
            '-1': 'passive',
        }
        key = table[str(sentiment)]
        cypher = "match (:%s {url : '%s'})<-[c:comment]-(:%s {url : '%s'}) set c.%s = c.%s+1" % (
            label, url, label, comment_url, key, key
        )
        return self._connect.run(cypher)
