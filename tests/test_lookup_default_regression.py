import click


def test_lookup_default_missing_returns_none():
    ctx = click.Context(click.Command("probe"), default_map={})
    assert ctx.lookup_default("email", call=False) is None


def test_lookup_default_existing_value_is_preserved():
    ctx = click.Context(click.Command("probe"), default_map={"email": "test@example.com"})
    assert ctx.lookup_default("email", call=False) == "test@example.com"


def test_lookup_default_callable_is_preserved():
    ctx = click.Context(click.Command("probe"), default_map={"email": lambda: "generated@example.com"})
    assert ctx.lookup_default("email", call=True) == "generated@example.com"
