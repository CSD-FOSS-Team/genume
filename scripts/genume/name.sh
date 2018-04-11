#!/bin/bash

git log --pretty="VALUES BAS authors \"%an %ce\"" | sort | uniq
