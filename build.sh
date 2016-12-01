#!/bin/bash
git diff --name-only HEAD~1

python -m unittest app.tests.test_sample
