import os

# get the input
message = os.environ.get("INPUT_NUM")

print(f"::set-output name=message::{message}")
