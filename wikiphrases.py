#!/usr/bin/env python
import fire
from corenlp import get_phrases

if __name__ == "__main__":
    fire.Fire(get_phrases)  # Use fire to create a command-line interface for get_phrases function