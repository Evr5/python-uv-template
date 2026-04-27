import os
import shutil
import subprocess
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv-init <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    template_url = "https://github.com/Evr5/python-uv-template.git"

    if os.path.exists(project_name):
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    print(f"Creating project '{project_name}' from template...")

    subprocess.run(["git", "clone", template_url, project_name], check=True)
    shutil.rmtree(os.path.join(project_name, ".git"), ignore_errors=True)

    toml_path = os.path.join(project_name, "pyproject.toml")
    if os.path.exists(toml_path):
        with open(toml_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content.replace('name = "python-uv-template"', f'name = "{project_name}"')

        with open(toml_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    subprocess.run(["git", "init"], cwd=project_name, check=True)

    print(f"Success! Your project is ready in ./{project_name}")
    print(f"Next steps:\n  cd {project_name}\n  uv sync")

if __name__ == "__main__":
    main()
