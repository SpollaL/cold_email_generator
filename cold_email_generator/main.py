import sys
import streamlit.web.cli as stcli
import cold_email_generator.app  # Ensure this is importable


def main():
    """Launch the Streamlit app."""
    # Dynamically determine the file path of the app module
    app_path = cold_email_generator.app.__file__

    # Set sys.argv to mimic a Streamlit command-line call
    sys.argv = ["streamlit", "run", app_path]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
