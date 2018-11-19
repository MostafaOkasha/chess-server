from setuptools import setup


setup(
    name="ChessServer",
    version="0.0.1",
    author="4TB6 Capstone Group",
    author_email="goyalr@mcmaster.ca",
    scripts=['scripts/play_ai.py'],
    packages=["serverapp"],
    url="https://github.com/robgoyal/chess-server",
    description="Simple chess server running Stockfish engine",
    long_description=open("README.md").read(),
    install_requires=["flask", "python-chess", "requests"],
    entry_points={
        'console_scripts': ['run-chess-server=run:main']
    }
)