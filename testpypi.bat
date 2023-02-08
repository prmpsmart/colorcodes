python -m build
twine check dist/*
@REM twine upload -r testpypi dist/* --verbose
