#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'random-string.py'
run_python_test 's 3' 'sss'
end_python_test
