from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from views import get_all_entries, get_single_entry, delete_entry, get_search_entry, create_entry, update_entry
from views import get_single_mood, get_all_moods




# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    
    

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)
        # (resource, searchTerm) = self.parse_url(self.path)# the resource = the url 
        #aka animal or locations and id equals the id of it. If there isn't an
        #id then line 86 else will pass

        if resource == "entries":
            if id is not None:
                response = f"{get_single_entry(id)}" 
            
            # elif searchTerm is not None:
            #     response = f"{get_search_entry(searchTerm)}"
            
            else:
                response = f"{get_all_entries()}"
        
        elif resource == "moods":
            if id is not None:
                response = f"{get_single_mood(id)}" 
            else:
                response = f"{get_all_moods()}"
 

        self.wfile.write(response.encode())
        
    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)
            
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0)) #content_len = the length of the item you are posting 
        post_body = self.rfile.read(content_len) #post_body equals the read file of content_len from above
        

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body) #changing the post_body gathered from above to a dictionary through json.loads.

        # Parse the URL
        (resource, id) = self.parse_url(self.path) #getting the response which is a dictionary

        # Initialize new animal
        new_entry = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "entries":
            new_entry = create_entry(post_body)       
      
        self.wfile.write(f"{new_entry}".encode())
        
    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "entries":
            success = update_entry(id, post_body)
        # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
            
        
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()