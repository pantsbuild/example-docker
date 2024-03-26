# Note that multistage buildx builds requires using the containerd image store, due to
# limitations with the docker-container driver (https://github.com/moby/buildkit/issues/2343)

docker_image(
    name="multiplatform-base",
    source="Dockerfile.base",
    skip_push=True,
    build_platform=["linux/amd64", "linux/arm64"],
)

docker_image(
    name="multiplatform-final",
    source="Dockerfile.final",
    build_platform=["linux/amd64", "linux/arm64"],
)
