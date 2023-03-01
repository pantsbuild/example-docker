# example-docker

An example repository to demonstrate Pantsbuild's experimental Docker support.

See [pantsbuild.org](https://www.pantsbuild.org/docs) for much more detailed documentation.

This is only one possible way of laying out your project with Pantsbuild. See
[pantsbuild.org/docs/source-roots#examples](https://www.pantsbuild.org/docs/source-roots#examples)
for some other example layouts.

Note: Pantsbuild and Pants will be used interchangebly, they refer to the same thing, the Pants
Build System.


# Running Pantsbuild

You run Pants goals using the `pants` launcher binary, which will bootstrap the
version of Pants configured for this repo if necessary.

See [here](https://www.pantsbuild.org/docs/installation) for how to install the `pants` binary.

Use `pants --version` to see the version of Pants configured for the repo (which you can also find
in `pants.toml`).


# Goals

Pants commands are called _goals_. You can get a list of goals with

```
pants help goals
```

Most goals take arguments to run on. To run on a single directory, use the directory name with `:`
at the end. To recursively run on a directory and all its subdirectories, add `::` to the end.

For example:

```
pants lint src/python/hello_world: src/docker::
```

You can run on all changed files:

```
pants --changed-since=HEAD lint
```

You can run on all changed files, and any of their "dependees":

```
pants --changed-since=HEAD --changed-dependees=transitive test
```


# Example Goals

Try these out in this repo!


## Run a Docker image

```
pants run src/docker/hello_world:python
pants run src/docker/hello_world:shell
```


## List targets

```
pants list ::  # All targets.
pants list 'src/**/*.py'  # Just targets containing Python code.
```


## Run linters and formatters

```
pants fmt lint ::  # First format, then lint all sources.
```


## Count lines of code

```
pants count-loc '**/*'
```


## Dynamic image tag

The documentation for [dynamic image
tagging](https://www.pantsbuild.org/docs/tagging-docker-images#using-env-vars-to-include-dynamic-data-in-tags)
has an example implementation here showcasing how it works.

```
DYNAMIC_TAG=$(date +%Y.%m.%d) pants package src/docker/dynamic_tags

10:47:43.89 [INFO] Completed: Building docker image dynamic_tags:1.0-2022.03.15
10:47:43.89 [INFO] Built docker image: dynamic_tags:1.0-2022.03.15
Docker image ID: sha256:8f6922aec0de7c147862672fa2cef4bd72f51e02b5a06089b0383355410b79f2

DYNAMIC_TAG=$(date +%Y.%m.%d) pants run src/docker/dynamic_tags
10:47:43.89 [INFO] Completed: Building docker image dynamic_tags:1.0-2022.03.15
  ____
| demo |
  ====
    \
     \
       ^__^
       (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```
