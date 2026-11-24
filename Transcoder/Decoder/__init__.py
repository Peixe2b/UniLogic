"""UniLogic output backends and bytecode decompiler."""

from importlib import import_module

_EXPORTS = {
    "decompile_bytes": (".ubi2ul", "decompile_bytes"),
    "decompile_file": (".ubi2ul", "decompile_file"),
    "generate_c": (".ul2c", "generate"),
    "generate_javascript": (".ul2js", "generate"),
    "generate_llvm": (".ul2llvm", "generate"),
    "generate_python": (".ul2py", "generate"),
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