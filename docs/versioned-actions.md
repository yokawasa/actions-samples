# How to refer versioned actions

If it's Public action, you can refer the action in this format `{owner}/{repo}@{ref}`
``` yaml
- name: test step
  uses: actions/aws@v2.0.1
```

You can refer a specific branch, ref, or SHA, etc.

```yaml
steps:    
  # Reference a specific commit
  - uses: actions/setup-node@74bc508
  # Reference the major version of a release
  - uses: actions/setup-node@v1
  # Reference a minor version of a release
  - uses: actions/setup-node@v1.2
  # Reference a branch
  - uses: actions/setup-node@master
```

If it's a public action in a subdirectory, you can refer the action in this format `{owner}/{repo}/{path}@{ref}`
```yaml
- name: test step
  uses: actions/aws/ec2@master
```

## Relevant links
- [example-using-versioned-actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#example-using-versioned-actions)

