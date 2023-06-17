# Copyright 2022 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

docker_image(
    name="python",
    source="Dockerfile.python",
)

docker_image(
    name="shell",
    source="Dockerfile.shell",
    # This dependency is not yet inferred from the Dockerfile.
    dependencies=["src/shell/hello_world"],
)

docker_image(
    name="codegen",
    source="Dockerfile.codegen",
    dependencies=[":hello_msg"],
    context_root="./",
)

shell_command(
    name="hello_msg",
    output_dependencies=["src/shell/hello_world"],
    outputs=["msg.txt"],
    command="../../shell/hello_world/main.sh > msg.txt",
    tools=["echo", "sh"],
)
