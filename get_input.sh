#!/usr/bin/bash
if [ -z "$1" ]; then
    echo "No day supplied"
    exit 1
fi

day=$1
cp -r template ./$day

echo "Downloading input for day $day..."
curl -H "Cookie: session=$AOC_25_COOKIE" "https://adventofcode.com/2025/day/$day/input" > ./$day/full_input.txt
echo "Done"

