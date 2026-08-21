#!/usr/bin/env python3
"""
Sync upstream skills from mattpocock/skills into .agents/skills/
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

UPSTREAM_REPO = "https://github.com/mattpocock/skills.git"
REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET_SKILLS_DIR = REPO_ROOT / ".agents" / "skills"

def main():
    print(f"Syncing upstream skills from {UPSTREAM_REPO}...")
    TARGET_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        clone_dir = Path(tmpdir) / "upstream-skills"
        subprocess.run(["git", "clone", "--depth", "1", UPSTREAM_REPO, str(clone_dir)], check=True)

        skills_dir = clone_dir / "skills"
        categories = ["engineering", "productivity", "misc", "in-progress"]
        synced_count = 0

        for cat in categories:
            cat_dir = skills_dir / cat
            if not cat_dir.exists():
                continue
            for skill_path in cat_dir.iterdir():
                if skill_path.is_dir():
                    dest_path = TARGET_SKILLS_DIR / skill_path.name
                    dest_path.mkdir(parents=True, exist_ok=True)
                    for item in skill_path.iterdir():
                        if item.is_dir():
                            shutil.copytree(item, dest_path / item.name, dirs_exist_ok=True)
                        else:
                            shutil.copy2(item, dest_path / item.name)
                    synced_count += 1

        print(f"Successfully synchronized {synced_count} skills into {TARGET_SKILLS_DIR}")

if __name__ == "__main__":
    main()
