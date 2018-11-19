from serverapp import app
from config import HOST, PORT, DEBUG


def main():
    # Run the server
    app.run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == "__main__":
    main()