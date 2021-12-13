#!/bin/bash
echo "Requests count:" > output.txt
grep -E 'POST|GET|PUT' access.log | wc -l >> output.txt
echo "Post request count:" >> output.txt
grep -o POST access.log | wc -w >> output.txt
echo "GET requests count:" >> output.txt
grep -o GET access.log | wc -w >> output.txt
echo "PUT requests count:" >> output.txt
grep -o PUT access.log | wc -w >> output.txt
