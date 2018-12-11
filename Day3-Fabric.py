from collections import defaultdict
from typing import List
import re


def read_input_file(filename: str) -> List[str]:
    input_file = open(filename)
    lines = input_file.readlines()
    input_file.close()
    return lines


def fabric1(filename: str):
    raw_claims = read_input_file(filename)
    claimed_points = defaultdict(int)
    total_overlapped_point = 0

    for claim in raw_claims:
        claim = list(map(int, re.findall(r'\d+', claim)))  # Parse the raw data into numbers only
        (number, startX, startY, width, height) = claim

        for x in range(startX, startX+width):
            for y in range(startY, startY+height):
                claimed_points[(x, y)] += 1  # Mark every point that get claimed

    for point in claimed_points:
        if claimed_points[point] >= 2:  # If the point is being marked more than once, it's overlapped
            total_overlapped_point += 1

    print(total_overlapped_point)


def fabric2(filename: str):
    raw_claims = read_input_file(filename)
    claimed_points = defaultdict(int)
    unique_point = 0

    for claim in raw_claims:
        claim = list(map(int, re.findall(r'\d+', claim)))  # Parse the raw data into numbers only
        (number, startX, startY, width, height) = claim

        for x in range(startX, startX+width):
            for y in range(startY, startY+height):
                claimed_points[(x, y)] += 1  # Mark every point that get claimed

    for claim in raw_claims:
        claim = list(map(int, re.findall(r'\d+', claim)))
        (number, startX, startY, width, height) = claim
        is_unique = True

        for x in range(startX, startX+width):
            if not is_unique:  # If this claim is marked as non-unique, no need to check further
                break

            for y in range(startY, startY+height):
                if claimed_points[(x, y)] > 1:  # If this point is overlapped, it's not unique
                    is_unique = False
                    break

        if is_unique:  # If this claim is unique, get the ID for an answer
            unique_point = number
            break

    print(unique_point)


fabric2("Day3-input.txt")