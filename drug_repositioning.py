import http.client
import json

class Drug_Repositioning:

    def __init__(self):
        self.base_url = 'drug-repositioning.com'
        self.headers = {'Content-type': 'application/json'}

    def get_nodes_autocomplete(self, 
                               keyword #Keyword to search for
                               ):
        """
        Get nodes that start with the query string.
        """

        conn = http.client.HTTPSConnection(self.base_url)
        conn.request("POST", "/api/auto-complete", json.dumps({"keyword": keyword}), self.headers)
        r1 = conn.getresponse()
        data1 = r1.read()
        conn.close()
        nodes = json.loads(data1)
        return nodes

    def get_cell_lines(self, 
                       keyword, #Keyword to search for
                       pertType, #Pertubation type, [SH, XPR or OE]
                    ):
        """
        Get cell lines for a given node name and pertubation type.
        """

        conn = http.client.HTTPSConnection(self.base_url)
        conn.request("POST", "/api/get-cell-lines", json.dumps({"keyword": keyword, "pertType": pertType}), self.headers)
        r1 = conn.getresponse()
        data1 = r1.read()
        conn.close()
        cell_lines = json.loads(data1)
        return cell_lines

    def get_query_data(self, 
                       node, # Node name to search for. #string
                       pertType, # Pertubation type, can be SH, XPR or OE. #string
                       isActivator, # Query for activators or inhibitors #boolean
                       cellLine = None, # Cell line to search for, if None, query spans all cell lines. Default: None #string
                       absoluteSimilarity = 0.4, # Absolute similarity threshold between 0 and 1. default: 0.4. #float
                       ):
        """
        Get data for a given node, pertubation type, and cell line.
        """

        conn = http.client.HTTPSConnection(self.base_url)
        conn.request("POST", "/api/query", json.dumps({"geneOrDrug": node, "pertType": pertType, "isActivator": isActivator, "cellLine": cellLine, "absoluteSimilarity": absoluteSimilarity}), self.headers)
        r1 = conn.getresponse()
        data1 = r1.read()
        conn.close()
        query_data = json.loads(data1)
        return query_data