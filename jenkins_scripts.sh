#!/bin/bash

touch ~/.pylintrc

echo " ************************************************************************************************"
echo " |                                      Problem 1: Unit Test                                    |"
echo " ************************************************************************************************"
python ./LAB\ B1/Problem\ 1/UnitTestEvenOdd.py

echo " ************************************************************************************************"
echo " |                                      Problem 1: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./LAB\ B1/Problem\ 1/HWproblemOne.py


echo " ************************************************************************************************"
echo " |                                      Problem 2: Unit Test                                    |"
echo " ************************************************************************************************"
python ./LAB\ B1/Problem\ 2/UnitTestListComparison.py

echo " ************************************************************************************************"
echo " |                                      Problem 2: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./LAB\ B1/Problem\ 2/HWproblemTwo.py

echo " ************************************************************************************************"
echo " |                                      Problem 3: Unit Test                                    |"
echo " ************************************************************************************************"
python ./LAB\ B1/Problem\ 3/testpalindrome.py

echo " ************************************************************************************************"
echo " |                                      Problem 3: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./LAB\ B1/Problem\ 3/palindrome.py

echo " ************************************************************************************************"
echo " |                                      Problem 4: Unit Test                                    |"
echo " ************************************************************************************************"
python ./LAB\ B1/Problem\ 4/testoverlap.py

echo " ************************************************************************************************"
echo " |                                      Problem 4: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./LAB\ B1/Problem\ 4/overlap.py

echo " ************************************************************************************************"
echo " |                                      Problem 5: Unit Test                                   |"
echo " ************************************************************************************************"
python ./reverseword_test.py

echo " ************************************************************************************************"
echo " |                                      Problem 5: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./reverseword.py 

echo " ************************************************************************************************"
echo " |                                      Problem 6: Unit Test                                    |"
echo " ************************************************************************************************"
python ./LAB\ B1/Problem\ 6/cowsbulls_test.py

echo " ************************************************************************************************"
echo " |                                      Problem 6: Pylint                                       |"
echo " ************************************************************************************************"
python -m pylint ./reverseword.py || exit 0
