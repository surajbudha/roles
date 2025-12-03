#!/usr/bin/env python3
"""
This module provides functions to hash password for prometheus.

"""
import sys # Import sys
import bcrypt # Import bcrypt

password = sys.argv[1]
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print(hashed_password.decode())
