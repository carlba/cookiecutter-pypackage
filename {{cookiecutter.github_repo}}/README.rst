{% for _ in cookiecutter.project_name %}={% endfor %}
# {{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Development Environment
-----------------------

.. sourcecode:: bash

    git clone git@github.com:{{ cookiecutter.github_user}}/{{ cookiecutter.github_repo}}.git
    virtualenv venv && source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
