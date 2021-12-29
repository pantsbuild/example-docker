# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from hello_world.main import main


def test_main(capsys) -> None:
    main()
    assert capsys.readouterr().out == "Hello World!\n"
