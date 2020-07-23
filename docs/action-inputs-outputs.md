# Action inputs and outputs

## Can action inputs be arrays?

> Action inputs only supports string keys and string values at this time. This is because they translate to environment variables within the action’s execution run.

(ref: https://github.community/t/can-action-inputs-be-arrays/16457)

## How to set output of the action in a docker container?

You can set output using `set-output` like this:
> endpoint.sh
```bash
#!/bin/sh -l

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"
```

> action.yml
```yaml
name: 'Hello World'
description: 'Greet someone and record the time'
inputs:
  who-to-greet:  # id of input
    description: 'Who to greet'
    required: true
    default: 'World'
outputs:
  time: # id of output
    description: 'The time we greeted you'
runs:
  using: 'docker'
  image: 'Dockerfile'
  args:
    - ${{ inputs.who-to-greet }}
```
(ref: https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action#create-an-action-metadata-file)
