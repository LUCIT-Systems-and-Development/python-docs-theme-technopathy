import os


def get_path():
    """Shortcut for users to access this theme. If you are using
    Sphinx < 1.7, you can add it into html_theme_path::
        import sphinx_typlog_theme
        html_theme_path = [sphinx_typlog_theme.get_path()]
    :return: theme path
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def setup(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme(
        'python_docs_theme_technopathy', current_dir)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
