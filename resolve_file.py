import os
from jsonspec.reference import Registry, resolve
from jsonspec.reference.providers import FilesystemProvider

dir_files = os.path.dirname(os.path.abspath(__file__))

obj = {"foo": {"$ref": "test:first.data1#/value3"}}

provider = FilesystemProvider(dir_files, prefix="test:")

resolved = resolve(
    obj, "#/foo", registry=provider
) 

print(resolved)