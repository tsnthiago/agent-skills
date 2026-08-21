#!/usr/bin/env python3
"""
Sync upstream skills from:
- https://github.com/mattpocock/skills.git
- https://github.com/Panniantong/agent-reach.git
- https://github.com/Graphify-Labs/graphify.git
into .agents/skills/
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET_SKILLS_DIR = REPO_ROOT / ".agents" / "skills"

UPSTREAMS = [
    {
        "name": "mattpocock/skills",
        "url": "https://github.com/mattpocock/skills.git",
        "type": "mattpocock"
    },
    {
        "name": "Panniantong/agent-reach",
        "url": "https://github.com/Panniantong/agent-reach.git",
        "type": "agent-reach"
    },
    {
        "name": "Graphify-Labs/graphify",
        "url": "https://github.com/Graphify-Labs/graphify.git",
        "type": "graphify"
    }
]

def sync_mattpocock(clone_dir: Path):
    skills_dir = clone_dir / "skills"
    categories = ["engineering", "productivity", "misc", "in-progress"]
    synced = 0
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
                synced += 1
    return synced

def sync_agent_reach(clone_dir: Path):
    skill_src = clone_dir / "agent_reach" / "skill"
    guides_src = clone_dir / "agent_reach" / "guides"
    dest_path = TARGET_SKILLS_DIR / "agent-reach"
    dest_path.mkdir(parents=True, exist_ok=True)

    if skill_src.exists():
        for item in skill_src.iterdir():
            if item.is_dir():
                shutil.copytree(item, dest_path / item.name, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest_path / item.name)
    
    if guides_src.exists():
        guides_dest = dest_path / "guides"
        guides_dest.mkdir(parents=True, exist_ok=True)
        for item in guides_src.iterdir():
            if item.is_dir():
                shutil.copytree(item, guides_dest / item.name, dirs_exist_ok=True)
            else:
                shutil.copy2(item, guides_dest / item.name)
    return 1

def sync_graphify(clone_dir: Path):
    skill_file = clone_dir / "graphify" / "skill.md"
    dest_path = TARGET_SKILLS_DIR / "graphify"
    dest_path.mkdir(parents=True, exist_ok=True)
    if skill_file.exists():
        shutil.copy2(skill_file, dest_path / "SKILL.md")
        return 1
    return 0

def main():
    TARGET_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    for upstream in UPSTREAMS:
        print(f"Syncing upstream from {upstream['name']} ({upstream['url']})...")
        with tempfile.TemporaryDirectory() as tmpdir:
            clone_dir = Path(tmpdir) / "repo"
            try:
                subprocess.run(["git", "clone", "--depth", "1", upstream["url"], str(clone_dir)], check=True)
                count = 0
                if upstream["type"] == "mattpocock":
                    count = sync_mattpocock(clone_dir)
                elif upstream["type"] == "agent-reach":
                    count = sync_agent_reach(clone_dir)
                elif upstream["type"] == "graphify":
                    count = sync_graphify(clone_dir)
                print(f"Successfully synced {count} skills from {upstream['name']}.")
            except Exception as e:
                print(f"Error syncing {upstream['name']}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
