# UI library testing

- Every component has a unit test (rendering, inputs, outputs) and a Storybook story with the main states
- Accessibility check (axe) runs in Storybook or tests; violations fail the build
- Visual states covered: loading, empty, error, populated
- Run test, lint and build and report real output before claiming done
