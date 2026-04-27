import os
import shutil
import subprocess
import sys

def check_uv() -> bool:
    """Check if uv is installed and available in PATH."""
    return shutil.which("uv") is not None

def install_uv() -> None:
    """Try to install uv using pip."""
    print("uv not found. Attempting to install uv...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=True)
        print("uv installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install uv automatically. Please install it manually: https://github.com/astral-sh/uv")
        sys.exit(1)

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv-init <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    template_url = "https://github.com/Evr5/python-uv-template.git"

    if os.path.exists(project_name):
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    if not check_uv():
        install_uv()

    print(f"🚀 Creating project '{project_name}' from template...")

    # Clone template and remove .git to avoid conflicts
    subprocess.run(["git", "clone", template_url, project_name], check=True)
    shutil.rmtree(os.path.join(project_name, ".git"), ignore_errors=True)

    # Update pyproject.toml with the new project name
    toml_path = os.path.join(project_name, "pyproject.toml")
    if os.path.exists(toml_path):
        with open(toml_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('name = "python-uv-template"', f'name = "{project_name}"')
        with open(toml_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    # Initialize a new git repository
    subprocess.run(["git", "init"], cwd=project_name, check=True)

    print(f"✅ Success! Your project is ready in ./{project_name}")
    print(f"Next steps:\n  cd {project_name}\n  uv sync")

if __name__ == "__main__":
    main()
