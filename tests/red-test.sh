#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'red.py'
run_python_test '""' 'False'
run_python_test 'red' 'True'
run_python_test 'aaa' 'False'
run_python_test 'blueredgreen' 'True'
end_python_test
