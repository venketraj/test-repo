# Project and Git Workflow: Calculator Example

This guide is for someone new to professional software development. It uses this calculator to show how to plan a small change, manage project files, use Git safely, and publish work through GitHub.

## 1. Understand the Project

Before changing code, find the project entry point, setup instructions, and dependency configuration:

- `main.py` contains the calculator and its command-line loop.
- `pyproject.toml` defines the Python project and dependencies.
- `uv.lock` records exact dependency versions for repeatable installs.
- `README.md` explains what the project does and how to run it.

For an existing checkout, install its dependencies with `uv sync`. Do not run `uv init` in this repository; `uv init` is for starting a new project. Add a dependency only when the code needs it, using `uv add PACKAGE_NAME` so the project configuration and lock file stay in sync.

## 2. Plan Work Before Coding

Start with an outcome that a user or teammate can verify. Keep the first change small enough to review, and write acceptance criteria before implementation.

Example feature request: **Add calculation history for the current session.**

Acceptance criteria:

- Each successful calculation is saved with its expression and result.
- A `history` command lists calculations made since the program started.
- Invalid expressions are not added to history.
- The README explains the new command.

Break the work into a few tasks: inspect the input loop, implement history storage and display, verify successful and invalid inputs, then update the documentation. If working with a team, put the request and acceptance criteria in a GitHub Issue so scope and progress are visible.

## 3. Know the Git States

- **Working tree:** files you have edited locally.
- **Staging area:** changes selected for the next commit.
- **Commit:** a named snapshot of staged changes.
- **Branch:** an independent line of work for a feature or fix.
- **Remote:** a copy of the repository hosted elsewhere, such as GitHub.

Use `git status` often. It shows the current branch and which changes are modified, staged, or untracked. Use `git diff` to inspect unstaged changes and `git diff --staged` to inspect what the next commit will contain.

## 4. Make a Change on Its Own Branch

For the example history feature, start from the latest `main` branch and create a descriptive branch:

```powershell
git switch main
git pull
git switch -c feature/calculation-history
```

Make the smallest useful implementation. Run the program and check the feature's acceptance criteria. For this calculator, a manual check can include a successful expression, `history`, an invalid expression, and `q`. Add automated tests when the project has a test suite or when the change warrants one.

Before committing, review and stage only the intended files:

```powershell
git status
git diff
git add main.py README.md
git diff --staged
```

If you created or changed a test file, stage it too. Staging specific files is safer than `git add .`, which can include unrelated work or local files. Then make a small commit with an action-oriented message:

```powershell
git commit -m "Add calculation history"
```

Other useful commit messages include `Fix division by zero handling` and `Document calculator setup`.

## 5. Push and Open a Pull Request

Push the feature branch to GitHub:

```powershell
git push -u origin feature/calculation-history
```

Open a pull request from that branch into `main`. In the pull request, summarize the change, list how you verified it, and link the related Issue. Review the diff, respond to feedback, and merge only after required checks pass. The branch can usually be deleted after it is merged.

## 6. Publish This Repository for the First Time

This project is already a local Git repository and has an initial commit. To publish it:

1. Create a new, empty repository on GitHub. Do not initialize it with another README, license, or `.gitignore`; this project already has its own files.
2. Check whether a remote is already configured:

	```powershell
	git remote -v
	```

3. If there is no `origin`, add the URL from the new GitHub repository. Replace the placeholders with your account and repository name:

	```powershell
	git remote add origin https://github.com/OWNER/REPOSITORY.git
	```

4. Rename the current branch to `main` and push it:

	```powershell
	git branch -M main
	git push -u origin main
	```

After this first push, `git push` sends later commits on the configured branch. GitHub may ask you to authenticate through your configured credential manager or browser. Never put a password or access token directly in a remote URL or commit it to the repository.

## 7. Everyday Guidelines

- Pull the latest shared changes before starting new work.
- Keep one branch focused on one feature, bug fix, or documentation task.
- Check `git status` and review diffs before staging and committing.
- Do not commit credentials, private data, virtual environments, or generated files. Keep local-only files in `.gitignore`.
- Commit working, understandable steps; do not wait until a large feature is complete to make the first commit.
- Keep the README accurate when setup, behavior, or commands change.
- If a command fails, read the full error and inspect the repository state before repeating commands that modify files or history.

## Quick Reference

```powershell
uv sync                              # Install project dependencies
uv run python main.py                # Run the calculator
git status                           # Check repository state
git diff                             # Review unstaged edits
git diff --staged                    # Review staged edits
git switch -c feature/short-name     # Start focused work
git add path/to/file                 # Stage selected work
git commit -m "Describe the change"  # Save a local snapshot
git push -u origin feature/short-name # Publish a branch
```