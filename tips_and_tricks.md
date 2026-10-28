## 15.1 Secure Third-Party Action References

Referencing actions using mutable Git tags (such as @v4) is convenient for learning. However, in high-security production environments, tags can theoretically be modified if an upstream maintainer account is compromised. Pinning to a specific commit SHA provides cryptographic supply-chain integrity

For critical pipelines, pin third-party actions to an immutable, full-length 40-character commit SHA, adding a comment indicating the version:

YAML
```
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```
Tools like Dependabot can automatically open pull requests to update these pinned commit SHAs when new action versions are released.
15.2 Maintain Minimal, Focused Jobs

Avoid packing my entire build, lint, test, container packaging, and deployment processes into one monolithic step. Breaking workflows into focused jobs with clear dependencies provides three key benefits:

    Pinpoints failures to a specific stage in the UI immediately.
    Enables parallel execution, reducing total pipeline duration.
    Allows me to apply fine-grained permissions to individual jobs.

15.3 Add Execution Timeouts

By default, GitHub Actions allows a job to run for up to six hours before terminating it. An unresponsive network request, hung test process, or prompt waiting for user input can tie up my runner needlessly.

Always set an explicit timeout-minutes limit on every job:

YAML
```
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15 # Terminate if execution exceeds 15 minutes
```
15.4 Concurrency and Run Cancellation

When developers push multiple commits in rapid succession to the same branch, running complete pipelines for every intermediate commit wastes compute time.

Use concurrency groups with cancel-in-progress: true to automatically cancel outdated workflow runs when a newer commit is pushed:

YAML
```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```