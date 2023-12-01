#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me
curl -sX PUT -L -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
