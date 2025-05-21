from jsonspec.reference import resolve

obj = {
    'foo': ['bar', 'baz', {
        '$ref': '#/sub'
    }],
    'sub': 'quux'
}

resolved = resolve(obj, '#/foo/2')

print(resolved)
