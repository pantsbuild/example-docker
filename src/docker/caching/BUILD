# Copyright 2022 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

docker_image(
    name="with-local-cache-backend",
    cache_to={"type": "local", "dest": "/tmp/docker-cache/pants-example"},
    cache_from={"type": "local", "src": "/tmp/docker-cache/pants-example"},
)
