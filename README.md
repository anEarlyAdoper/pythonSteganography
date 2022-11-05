# Python Steganography

This project developed in Python uses the steganography technique to hide text in images.

## Getting Started

These instructions will give you some help in order to run the program on your PC.

### Prerequisites

For running the project is important to have Python installed on your PC. You can get it from the [Python official web page](https://www.python.org/downloads/).

### Entering the virtual environment

A step by step series of examples that tell you how to execute the program by entering on the virtual environment. Once the git is pulled:

First you need to enter de virtual environment by entering in "venv/Scripts" from the terminal. Once in execute

    activate.bat

Note: you will see that the cmd prompt changes to "(venv)"

## Running the code

once entered on the virtual environment, navigate usign

    cd ..

until you arrive to the main directory of the project (where main.py is located)

Then, just run

    main.py

To execute the code.

## The code

Once started the program it will display the images located in the 'images' directory.
All the images displayed there could be used for steganography but they have to meet certain requirements that are also displayed.

After selecting the image you will be prompted with a menu showing:

    save, read or delete content

####save

Selecting this option will encrypt some text with a given password on to the photo, the algorithm is quite complex,
so don't suffer for random people to decrypt it without the password. Is important to not modify or compress the photo 
because it may delete the information you stored.

####read

Selecting this option will decrypt (if there's something saved) the photo with a given password. The photo will remain intact,
so you can read it multiple times.

####delete content

Selecting this option will "clean" the image from any possible message stored, once deleted, the information can't be recovered.


###Extra: music

You will notice that there's some music running in the background while the program executes, you can stop it by deleting the
audio file from de 'audio' directory. If you want to simply change the melody you can save a mp3 file in that same directory and 
name it 'audio.mp3'.

## Exiting the virtual environment

Once you finished with the code, you can exit the virtual environment from the command line with

    deactivate

## Authors

  - **Arturo Moseguí** -
    [GitHub](https://github.com/anEarlyAdoper/)
  

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details