# Phase 1: Foundation and Project Setup

Phase 1 establishes the structure and publishing workflow for this ROS 2 learning portfolio. The goal is a site that a technical reviewer can understand quickly and a repository that can grow with runnable engineering work.

## Objectives

- Define a clear path from ROS 2 fundamentals to mobile manipulation.
- Publish documentation through Sphinx and GitHub Pages.
- Keep future examples, diagrams, and technical notes organized.
- Treat each learning milestone as evidence rather than an unverified skill claim.

## Completed Foundation

- The repository has dedicated locations for documentation, examples, and diagrams.
- The README introduces the portfolio and links to the published documentation.
- The roadmap covers five stages from foundation through community refinement.
- GitHub Actions builds the Sphinx site and deploys it to GitHub Pages.
- The project targets ROS 2 Jazzy Jalisco.
- The portfolio includes a professional profile link and an example contribution guide.

## Repository Structure

```text
.
|-- README.md
|-- phases.md
|-- assets/
|   `-- diagrams/
|-- docs/
|   `-- source/
|       |-- index.md
|       `-- phases/
|-- examples/
`-- requirements.txt
```

## Evidence Standard

A topic is complete when it includes at least one concrete artifact:

- runnable code or a reproducible command sequence
- a diagram that explains an architecture or data flow
- a test, expected output, or validation result
- a short engineering note that records a decision and its tradeoffs

## Environment Baseline

Examples target **ROS 2 Jazzy Jalisco**. The operating system and required packages will be recorded in each example's README so another engineer can reproduce the result.

See the [examples guide](https://github.com/r-jeremiah/ros2-roadmap/blob/main/examples/README.md) for the file layout and implementation checklist to use when adding an example.

## Next Milestones

1. Add the first runnable publisher/subscriber example under `examples/`.
2. Document setup, execution, expected output, and validation for that example.
3. Publish Phase 2 content covering ROS 2 nodes and communication.
