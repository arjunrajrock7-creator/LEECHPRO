import os
import subprocess
import sys
from logging import basicConfig, info, error, INFO, StreamHandler

basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[StreamHandler()],
    level=INFO,
)

def run_command(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True)

def update_repo():
    upstream_repo = os.environ.get("UPSTREAM_REPO", "").strip()
    upstream_branch = os.environ.get("UPSTREAM_BRANCH", "wzv3").strip()

    if not upstream_repo:
        info("No UPSTREAM_REPO provided or it is empty. Skipping auto-update.")
    else:
        info(f"Syncing with {upstream_repo} (branch: {upstream_branch})...")
        if os.path.exists(".git"):
            run_command("rm -rf .git")

        commands = [
            "git init -q",
            "git config --global user.email 'bot@htbotz.local'",
            "git config --global user.name 'hemanth-bot-Deployer'",
            "git add .",
            'git commit -sm "local-backup" -q',
            f"git remote add origin {upstream_repo}",
            "git fetch origin -q",
            f"git reset --hard origin/{upstream_branch} -q"
        ]

        success = True
        for cmd in commands:
            res = run_command(cmd)
            if res.returncode != 0 and "local-backup" not in cmd:
                error(f"Command failed: {cmd}")
                error(f"Error: {res.stderr}")
                success = False
                break

        if success:
            info("Successfully synced with UPSTREAM_REPO.")
        else:
            error("Failed to sync with UPSTREAM_REPO. Continuing with local files.")

    # Update requirements if requested
    update_pkgs = os.environ.get("UPDATE_PKGS", "True").lower() == "true"
    if update_pkgs and os.path.exists("requirements.txt"):
        info("Checking for package updates...")
        subprocess.call([sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"])

if __name__ == "__main__":
    update_repo()
