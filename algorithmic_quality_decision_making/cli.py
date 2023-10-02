from typing import Any

from click import Context, Parameter, echo, option, command

from algorithmic_quality_decision_making import __version__ as app_version


def _print_version(
        context: Context,
        _parameter: Parameter,
        value: Any,
) -> None:
    if not value or context.resilient_parsing:
        return
    echo(app_version)
    context.exit()


@command()
@option(
    "-V", "--version",
    is_flag=True,
    callback=_print_version,
    expose_value=False,
    is_eager=True,
)
def cli() -> None:
    pass
