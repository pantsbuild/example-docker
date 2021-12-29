# -*- python -*-

docker_image(name="python", source="Dockerfile.python")

docker_image(
    name="shell",
    source="Dockerfile.shell",
    # This dependency is not yet inferred from the Dockerfile.
    dependencies=["src/shell/hello_world"],
)
