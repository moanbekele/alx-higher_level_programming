#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
    Only installed pakage requests
    prints response with tabulation before -
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status") # GET urls req

    print("Body response:")
    print("\t- type: {}".format(type(r.text))) # Output <class 'str'>$
    print("\t- content: {}".format(r.text)) # Output content: OK$
