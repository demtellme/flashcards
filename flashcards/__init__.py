import os
BASEDIR = os.path.dirname(__file__)
FOLDER = os.path.join(BASEDIR, ".flashcardsfolder")
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
