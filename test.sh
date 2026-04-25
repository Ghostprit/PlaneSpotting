#!/bin/bash

HTTP_CODE=$(curl -o /dev/null -s -w "%{http_code}" http://localhost/health)

if [ "$HTTP_CODE" -eq 200 ]; then
    echo "Health check passed: HTTP $HTTP_CODE"
else
    echo "Health check failed: HTTP $HTTP_CODE"
    exit 1
fi