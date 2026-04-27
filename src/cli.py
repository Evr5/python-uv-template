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

    print(f"Creating project '{project_name}' from template...")

    subprocess.run(["git", "clone", template_url, project_name], check=True)
    shutil.rmtree(os.path.join(project_name, ".git"), ignore_errors=True)
    subprocess.run(["git", "init"], cwd=project_name, check=True)

    print(f"Success! Your project is ready in ./{project_name}")
    print(f"Next steps:\n  cd {project_name}\n  uv sync")

if __name__ == "__main__":
    main()
