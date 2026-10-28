# Level 1: Git and Version Control Fundamentals

    * Objective: Master basic branch management, commits, and pull requests from the command line.
    * Hands-on Task: Create a new repository. Create and switch to a feature branch, make three small commits, push the branch to GitHub, and open a pull request.
    * Verification: The pull request merges cleanly into the main branch via GitHub’s web interface.

# Level 2: First Workflow Creation

    * Objective: Understand workflow YAML syntax, directory structures, and the GitHub Actions dashboard.
    * Hands-on Task: Add a .github/workflows/hello.yml file that triggers on push and runs a simple shell step printing the runner OS and commit SHA.
    * Verification: The job finishes with a green checkmark in the Actions dashboard, and the logs display the correct output.

# Level 3: Automated Testing Integration

    * Objective: Set up language runtimes, install dependencies, and execute automated tests in a pipeline.
    * Hands-on Task: Configure a workflow that sets up Python, Node.js, or Go, installs dependencies from a lockfile, and runs a unit test suite.
    * Verification: Introduce an intentional assertion failure into your test suite; confirm that the workflow fails and highlights the broken test in the logs.

# Level 4: Pull Request Quality Gates

    * Objective: Protect default branches using automated pull-request validation.
    * Hands-on Task: Configure a workflow triggered by pull_request events and set up a branch protection rule requiring the job to pass before merging.
    * Verification: Open a pull request containing broken code; confirm that GitHub disables the merge button until a fixing commit is pushed.

# Level 5: Multi-Job Pipelines and Artifacts

    * Objective: Build multi-stage pipelines that run independent tasks concurrently and sequential tasks using needs.
    * Hands-on Task: Create a workflow with parallel linting and testing jobs, followed by a dependent packaging job that archives build outputs via actions/upload-artifact.
    * Verification: The lint and test jobs execute simultaneously, the package job starts only after both pass, and the output archive is available for download.

# Level 6: Security and Environment Configuration

    * Objective: Manage sensitive credentials safely and apply least-privilege token permissions.
    * Hands-on Task: Create an encrypted repository secret. Configure a workflow that reads this secret inside an environment variable, using minimal permissions blocks.
    * Verification: The workflow reads the secret successfully, masks its value in the logs with ***, and runs without excess token permissions.

# Level 7: Delivery and Deployment

    * Objective: Automate application deployments to a dedicated staging or hosting environment.
    * Hands-on Task: Deploy a static web dashboard, API documentation site, or container image to a service like GitHub Pages.
    * Verification: Pushing a change to main automatically updates the live deployment, verified by viewing the updated timestamp on the live UR* L.

# Level 8: Capstone Portfolio Project

    * Objective: Combine testing, multi-job coordination, security controls, and automated deployment into an end-to-end, documented project.
    * Hands-on Task: Build a complete repository containing a sample application, comprehensive tests, a multi-stage pipeline, and clear README documentation explaining your architectural decisions.
    * Verification: An external peer can clone the repository, open a pull request, observe automated checks running, and review the live deployed output.
