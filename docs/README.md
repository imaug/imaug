# imaug documentation

## prepare environment
```
conda create -n imaug-docs python=3.13 -
conda activate imaug-docs
pip install .
pip install -r docs/requirements.txt
```


To generate the image assets run in the document root folder
```bash
python docs/scripts/generate_all.py --all
```

Then generate the documentation by switching to the `docs` folder and run the make script:
```bash
cd docs
make html
```

Note that when calling `make html` you will probably get lots of warnings saying
`WARNING: toctree contains reference to nonexisting document (...)`. That is normal.
Just ignore these messages.
