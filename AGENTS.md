# AGENTS

## Purpose
This repository is a minimal Python tutorial workspace containing a few standalone scripts under `numbers/`.
There is no package metadata, no tests, and no existing developer documentation in the workspace.

## What agents should know
- The codebase is simple and script-based: `numbers/first tutorial/numbers1.py` and `numbers/first tutorial/strings/strings.py` are standalone examples.
- The examples use basic Python syntax and direct `print()` output.
- There is currently no audio-related code, module, or dependency in the repository.
- There is no `requirements.txt`, no `setup.py`, and no standard build/test workflow.

## Audio-related requests
- The user specifically asked about `audio`, but the current repository contains no audio features.
- For audio work, prefer adding a new tutorial area such as `audio/` or `numbers/audio/` rather than changing unrelated tutorial files.
- Keep audio examples lightweight and aligned with the existing style: small standalone Python scripts.

## Practical guidance
- Run individual scripts with the local Python interpreter, for example:
  - `python "numbers/first tutorial/numbers1.py"`
- Avoid adding unnecessary project structure unless the user expressly asks for it.
- If new functionality is added, keep file names simple and avoid adding spaces to new directory names when possible.

## Agent behavior
- Do not assume a complex project structure or test framework exists.
- Ask the user for clarification before implementing non-trivial features or reorganizing the repository.
