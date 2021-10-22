__license__ = "GPL"
__version__ = "just_a_draft"
__maintainer__ = "Gabriel Cerioni"
__email__ = "gacerioni@gmail.com"
__status__ = "just_a_draft"

# You just need this to execute the Script
# 1-) Python3.6+
# 2-) The std modules from the imports (I can provide requirements.txt later)
# 3-) Make sure to -pip install gql- ---- (GraphQL Module for Python) https://pypi.org/project/gql/
# 4-) Fix the API_KEY, or export it as an Env Variable - Line 30 or Line 32
# 5-) and finally, just `python3 program_name.py`

# I can help to enhance this later, this was a very quick work to help the CSM Team.

import re
import os
import random
import logging

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import log as requests_logger

# Configs (if this gets bigger, I'll provide a config file... or even Hashicorp Vault)
# logging.basicConfig(filename='gabs_graphql.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
requests_logger.setLevel(logging.WARNING)

API_KEY = "U1NIeUpod2tTMXltOXdTTEd5dzJhdzo6M0tvbTE4eG0zUzRiekc5NDN0UE1DeTV0VElpUjdPVlNkeTJUOERPeGRNR3ZNMW0xTkQyZjViNU1JZkkzQnJ2R2ZQZDd0VGpoRmFoa3RsVHQ="
API_ENDPOINT = "https://app.harness.io/gateway/api/graphql?accountId=bbk2i5CwSFSv6s3-Le0DbA"
#API_KEY = os.environ.get('HARNESS_GRAPHQL_API_KEY')
#API_ENDPOINT = os.environ.get('HARNESS_GRAPHQL_ENDPOINT')


def generic_graphql_query(query):
    req_headers = {
        'x-api-key': API_KEY
    }

    _transport = RequestsHTTPTransport(
        url=API_ENDPOINT,
        headers=req_headers,
        use_json=True,
    )

    # Create a GraphQL client using the defined transport
    client = Client(transport=_transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    generic_query = gql(query)

    # Execute the query on the transport
    result = client.execute(generic_query)
    return result

def get_all_instances_by_service_by_env():
    query = '''{
    instanceStats(groupBy: [{entityAggregation: Service}, {entityAggregation: Environment}]) {
       ... on StackedData {
         dataPoints {
           key {
             name
           }
           values {
             key {
               name
             }
             value
           }
         }
   
       }
     }
    }'''
    generic_query_result = generic_graphql_query(query)

    return(generic_query_result)


if __name__ == '__main__':
    logging.info("Starting the Program...")

    logging.info("Running our brainstorming query, we are not sure if this covers everything you need!")
    result_from_query = get_all_instances_by_service_by_env()
    print("")
    print(result_from_query)
    logging.info("Program Exited!")
