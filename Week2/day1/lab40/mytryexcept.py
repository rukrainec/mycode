#!/usr/bin/env python3
#29 May 2018, lab 40 pt2
while(True):
    try: # code we want to try to run goes under the try
        print("This is an error detection simulator.\nPlease select the error you'd like to simulate:")
        err = input('A= divide by zero\nB= IO\nC= failed Assertion\nD= Failed Attribute\nE= End of File\nF= Bad Import\nG= Ctrl+C\nH= Hit tab\nQ= quit \n')
        if err.upper() == 'A': raise ZeroDivisionError
        if err.upper() == 'B': raise IOError
        if err.upper() == 'C': raise AssertionError
        if err.upper() == 'D': raise AttributeError
        if err.upper() == 'E': raise EOFError
        if err.upper() == 'F': raise ImportError
        if err.upper() == 'G': raise KeyboardInterrupt
        if err.upper() == 'H': raise IndentationError
        if err.upper() == 'Q': break
        else: print('Bad input!')
    except ZeroDivisionError:  # Only catches div by zero errors
        print("Computers do not like div by zero")
    except IOError:
        print("This code raised an IO error")
    except AssertionError:
        print('Assertion Error detected!')
    except AttributeError:
        print('Attribute Error detected!')
    except EOFError:
        print('End of File Error detected!')
    except ImportError:
        print('Import Error detected!')
    except KeyboardInterrupt:
        print('You hit ^C!')
    except IndentationError:
        print('Spaces not tabs!')
    except:
        print("We're sorry, something unexpected happened. See your IT department.")
print('Thanks for playing!')