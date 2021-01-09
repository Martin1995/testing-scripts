#!/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test #some imports of HTTP server
import sys #import of sytem functions

class CORSRequestHandler (SimpleHTTPRequestHandler): #building a request handler
    def end_headers (self): #creating headers function
        self.send_header('Access-Control-Allow-Origin', '*') #header function sends CORS header with allow everything attribute (*) replace the [*] with a URL to restrict access
        SimpleHTTPRequestHandler.end_headers(self) #end of header function section

if __name__ == '__main__': #main function
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000) #looking for a user input that defines the port and otherwise use port 8000
#this entire python script was copied from a website after some intense google search!!
