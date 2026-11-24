"""UniLogic input converters and bytecode encoder."""

from importlib import import_module

_EXPORTS = {
    "transpile_c": (".c2ul", "translate_file"),
    "transpile_python": (".py2ul", "transpile"),
    "encode_bytecode": (".ul2ubi", "generate"),
}
__all__ = list(_EXPORTS)


def __getattr__(name):
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name, __name__), attribute_name)
    globals()[name] = value
    return value