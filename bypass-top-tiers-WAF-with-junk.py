from mitmproxy import http
import json
from collections import OrderedDict

def request(flow: http.HTTPFlow) -> None:
    # Check if the request is of type application/json
    content_type = flow.request.headers.get('Content-Type', '')
    
    if 'application/json' in content_type:
        try:
            # Attempt to parse the JSON body
            body_json = json.loads(flow.request.text, object_pairs_hook=OrderedDict)
        except Exception as e:
            # Skip processing if there's an error in parsing JSON
            print(f"Error processing JSON: {e}")
            return

        # Insert the new key-value pair at the top
        new_body_json = OrderedDict([('daviMariano', '0' * 132000)] + list(body_json.items()))

        # Convert JSON back to a string and update the request body
        flow.request.text = json.dumps(new_body_json)
