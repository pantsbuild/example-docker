# Copyright 2022 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

docker_image(
    name="with-gha-cache-backend",
    cache_to={"type": "gha", "mode": "max"},
    cache_from={"type": "gha"},
)
