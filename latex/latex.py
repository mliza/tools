import argparse
import IPython

def _parse_args():
    """
    Parse command-line arguments for LaTeX project generation.
    Returns an argparse.Namespace.
    """
    parser = argparse.ArgumentParser(
        description="Generate various LaTeX project structures."
    )

    # Mutually exclusive project type selection
    project = parser.add_mutually_exclusive_group(required=True)
    project.add_argument('-notes', action='store_true',
                         help='Generate a class notes project')
    project.add_argument('-homework', action='store_true',
                         help='Generate a homework project')
    project.add_argument('-beamer', action='store_true',
                         help='Generate a beamer presentation project')
    project.add_argument('-cheat', action='store_true',
                         help='Generate a cheat sheet project')

    return parser.parse_args()





if __name__=="__main__":
    arguments = _parse_args()
