#!/usr/bin/env python3

import os
import json
import wmill

# You can import any package from PyPI, even if the assistant complains

"""
Use Cmd/Ctrl + S to autoformat the code. Reset content in the bar to start from a clean template.
The client is used to interact with windmill itself through its standard API.
One can explore the methods available through autocompletion of `wmill.XXX`.
"""

import requests

AMIIBO_API = "https://www.amiiboapi.com/api/"

def main(
         name = "Put an amiibo name here"):
    """A main function is required for the script to be able to accept arguments.
    Types are recommended."""
    r = requests.get(f"{AMIIBO_API}/amiibo?name={name}")
    print(f"found {r.json()}")
    # retrieve variables, including secrets by querying the windmill platform.
    # secret fetching is audited by windmill.

    try:
      secret = wmill.get_variable("g/all/pretty_secret")
    except:
      secret = "No secret yet at g/all/pretty_secret!"

    print(f"The variable at `g/all/pretty_secret`: {secret}")

    # Get last state of this script execution by the same trigger/user
    last_state = wmill.get_state()
    new_state = {"foo": 42} if last_state is None else last_state
    new_state["foo"] += 1
    wmill.set_state(new_state)

    # fetch reserved variables as environment variables
    user = os.environ.get("WM_USERNAME")
    # the return value is then parsed and can be retrieved by other scripts conveniently
    return {"amiibo": name.split(), "user": user, "state": new_state}

if __name__ == '__main__':
    import sys
    from unittest.mock import MagicMock
    wmill = MagicMock()
    main(sys.argv[1])
