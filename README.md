# my-model-serving
모델 서빙 테스트용 코드


## Set virtual environment

```bash
# install virtualenv
pip install virtualenv

# create virtualenv
virtualenv .venv --python=3.9

# activate
source .venv/bin/activate

# install libraries
pip install -r requirements.txt

# deactivate
deactivate
```


## How to package project
```bash
python setup.py sdist

# how to install local package
pip install dist/my-model-serving-0.0.1.tar.gz

# how to upload package to pypi
twine upload --repository-url {target} dist/my-model-serving-0.0.1.tar.gz

# how to install package from remote
pip install --index-url {target} my-model-serving
```