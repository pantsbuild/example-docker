# Copyright 2022 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# Example how to provide dynamic data to the built image tag. Demo for documentation at
# https://www.pantsbuild.org/docs/tagging-docker-images#using-env-vars-to-include-dynamic-data-in-tags

docker_image(
    # Build args may also be provided globally for all `docker_image` targets under
    # `[docker].build_args` in pants.toml.
    extra_build_args=["DYNAMIC_TAG"],
    image_tags=["1.0-{build_args.DYNAMIC_TAG}"],
    instructions=[
        # In case the value is only optionally provided from the environment, a default value may be
        # provided in the Dockerfile instruction, while still being overridable from the environment.
        #
        # "ARG DYNAMIC_TAG=default",
        "FROM python:3.8",
        "RUN pip install --no-cache-dir cowsay==4.0",
        'CMD ["cowsay", "demo"]',
    ],
)
